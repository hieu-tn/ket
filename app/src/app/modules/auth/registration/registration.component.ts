import { Component, OnDestroy, OnInit, ViewChild } from '@angular/core';
import { Store } from '@ngrx/store';
import { FormControl, FormGroup, Validators } from '@angular/forms';

import { IAppState } from '@/state/state.models';
import { BlockScrollStrategy, Overlay } from '@angular/cdk/overlay';
import { MAT_SELECT_SCROLL_STRATEGY } from '@angular/material/select';
import * as authActions from '@/state/auth/auth.actions';
import {
  IGetVerificationPayloadAction,
  IRegistrationPayloadAction, IVerification, IVerifyCode,
  IVerifyCodePayloadAction
} from '@/state/auth/auth.models';
import { Subject } from 'rxjs';
import { authSelectors } from '@/state/auth/auth.selectors';
import { takeUntil } from 'rxjs/operators';
import { Router } from '@angular/router';
import { APP_URLS } from '@/constants/urls';
import { AuthTypes } from '../auth.models';
import { MatStepper } from '@angular/material/stepper';
import { CodeRegexValidator, formControlError, PhoneRegexValidator } from '@/modules/shared/validators/form.validators';


export function scrollFactory(overlay: Overlay): () => BlockScrollStrategy {
  return () => overlay.scrollStrategies.block();
}

@Component({
  selector: 'app-registration',
  templateUrl: './registration.component.html',
  styleUrls: ['./registration.component.scss'],
  providers: [
    {provide: MAT_SELECT_SCROLL_STRATEGY, useFactory: scrollFactory, deps: [Overlay]}
  ]
})
export class RegistrationComponent implements OnInit, OnDestroy {

  @ViewChild(MatStepper) stepper!: MatStepper;

  verificationForm: FormGroup = new FormGroup({});
  isVerificationFormSubmitted: boolean = false;
  codeForm: FormGroup = new FormGroup({});
  isCodeFormSubmitted: boolean = false;
  registrationForm: FormGroup = new FormGroup({});
  authTypes = ['SMS', 'MAIL'];
  formControlError = formControlError;

  private ngUnsubscribe = new Subject();
  private sessionToken: string = '';

  constructor(private store: Store<IAppState>,
              private router: Router) { }

  ngOnInit(): void {
    this.initForms();
    this.subscriber();
  }

  ngOnDestroy(): void {
    this.ngUnsubscribe.next();
    this.ngUnsubscribe.complete();
    this.clearActions();
  }

  onVerificationFormSubmit(): void {
    if (this.verificationForm.invalid) return;

    const payload: IGetVerificationPayloadAction = this.verificationForm.value;
    this.store.dispatch(authActions.getVerification(payload));
  }

  onCodeFormSubmit(): void {
    if (this.codeForm.invalid || !this.isVerificationFormSubmitted) return;

    const payload: IVerifyCodePayloadAction = {
      ...this.codeForm.value,
      sessionToken: this.sessionToken
    };
    this.store.dispatch(authActions.verifyCode(payload));
  }

  onRegistrationFormSubmit(): void {
    if (this.registrationForm.invalid || !this.isVerificationFormSubmitted || !this.isCodeFormSubmitted) return;

    const payload: IRegistrationPayloadAction = {
      ...this.registrationForm.value,
      sessionToken: this.sessionToken
    };
    this.store.dispatch(authActions.registration(payload));
  }

  onResetClick(): void {
    this.verificationForm.enable();
    this.verificationForm.reset({
      authType: {value: ''},
      target: {value: '', disabled: true}
    });
    this.isVerificationFormSubmitted = false;
    this.codeForm.disable();
    this.codeForm.reset();
    this.isCodeFormSubmitted = false;
    this.registrationForm.disable();
    this.registrationForm.reset();
  }

  private initForms(): void {
    this.verificationForm = new FormGroup({
      authType: new FormControl('', [Validators.required]),
      target: new FormControl({value: '', disabled: true}),
    });

    this.verificationForm.controls.authType.valueChanges
      .subscribe(selectedAuthType => {
        if (selectedAuthType === AuthTypes.MAIL) {
          this.verificationForm.controls.target.clearValidators();
          this.verificationForm.controls.target.addValidators([Validators.required, Validators.email]);
        } else {
          this.verificationForm.controls.target.clearValidators();
          this.verificationForm.controls.target.addValidators([Validators.required, PhoneRegexValidator()]);
        }
        this.verificationForm.controls.target.enable();
        this.verificationForm.controls.target.updateValueAndValidity();
      });

    this.codeForm = new FormGroup({
      code: new FormControl('', [Validators.required, CodeRegexValidator(), Validators.maxLength(6), Validators.minLength(6)])
    });
    this.codeForm.disable();

    this.registrationForm = new FormGroup({
      password: new FormControl('', [Validators.required])
    });
    this.registrationForm.disable();
  }

  private subscriber(): void {
    this.store.select(authSelectors.verification)
      .pipe(
        takeUntil(this.ngUnsubscribe)
      )
      .subscribe((data: IVerification) => {
        if (data) {
          this.verificationForm.disable();
          this.isVerificationFormSubmitted = true;
          this.sessionToken = data.sessionToken;
          this.codeForm.enable();
          this.stepper.next();
        }
      });

    this.store.select(authSelectors.verifyCode)
      .pipe(
        takeUntil(this.ngUnsubscribe)
      )
      .subscribe((data: IVerifyCode) => {
        if (data) {
          this.codeForm.disable();
          this.isCodeFormSubmitted = true;
          this.sessionToken = data.sessionToken;
          this.registrationForm.enable();
          this.stepper.next();
        }
      });

    this.store.select(authSelectors.registration)
      .pipe(
        takeUntil(this.ngUnsubscribe)
      )
      .subscribe((data: boolean) => {
        if (data) {
          this.router.navigateByUrl(APP_URLS.login);
        }
      });
  }

  private clearActions(): void {
    this.store.dispatch(authActions.clearGetVerification());
    this.store.dispatch(authActions.clearVerifyCode());
    this.store.dispatch(authActions.clearRegistration());
  }
}
