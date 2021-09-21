import { Component, OnDestroy, OnInit } from '@angular/core';
import { Store } from '@ngrx/store';
import { FormControl, FormGroup, Validators } from '@angular/forms';

import { IAppState } from '@/state/state.models';
import { BlockScrollStrategy, Overlay } from '@angular/cdk/overlay';
import { MAT_SELECT_SCROLL_STRATEGY } from '@angular/material/select';
import * as authActions from '@/state/auth/auth.actions';
import {
  IGetVerificationDispatchAction,
  IRegistrationDispatchAction,
  IVerifyCodeDispatchAction
} from '@/state/auth/auth.models';
import { Subject } from 'rxjs';
import { authSelectors } from '@/state/auth/auth.selectors';
import { takeUntil } from 'rxjs/operators';
import { Router } from '@angular/router';
import { APP_URLS } from '@/constants/urls';


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

  verificationForm: FormGroup = new FormGroup({});
  isVerificationFormSubmitted: boolean = false;
  codeForm: FormGroup = new FormGroup({});
  isCodeFormSubmitted: boolean = false;
  registrationForm: FormGroup = new FormGroup({});
  authTypes = ['SMS', 'MAIL'];

  private ngUnsubscribe = new Subject();
  private sessionToken: string = '';

  constructor(private store: Store<IAppState>, private router: Router) { }

  ngOnInit(): void {
    this.initForms();
    this.subscriber();
  }

  ngOnDestroy(): void {
    this.ngUnsubscribe.next();
    this.ngUnsubscribe.complete();
  }

  onVerificationFormSubmit() {
    if (this.verificationForm.invalid) return;

    const payload: IGetVerificationDispatchAction = this.verificationForm.value;
    this.store.dispatch(authActions.getVerification(payload));
  }

  onCodeFormSubmit() {
    if (this.codeForm.invalid || !this.isVerificationFormSubmitted) return;

    const payload: IVerifyCodeDispatchAction = {
      ...this.codeForm.value,
      sessionToken: this.sessionToken
    };
    this.store.dispatch(authActions.verifyCode(payload));
  }

  onRegistrationFormSubmit() {
    if (this.registrationForm.invalid || !this.isVerificationFormSubmitted || !this.isCodeFormSubmitted) return;

    const payload: IRegistrationDispatchAction = {
      ...this.registrationForm.value,
      sessionToken: this.sessionToken
    };
    this.store.dispatch(authActions.registration(payload));
  }

  onResetClick() {
    this.verificationForm.reset();
    this.isVerificationFormSubmitted = false;
    this.codeForm.reset();
    this.isCodeFormSubmitted = false;
    this.registrationForm.reset();
  }

  private initForms() {
    this.verificationForm = new FormGroup({
      authType: new FormControl('', [Validators.required]),
      target: new FormControl('', [Validators.required]),
    });
    this.codeForm = new FormGroup({
      code: new FormControl('', [Validators.required])
    });
    this.registrationForm = new FormGroup({
      password: new FormControl('', [Validators.required])
    });
  }

  private subscriber() {
    this.store.select(authSelectors.verification)
      .pipe(
        takeUntil(this.ngUnsubscribe)
      )
      .subscribe(data => {
        if (data) {
          this.isVerificationFormSubmitted = true;
          this.sessionToken = data.sessionToken;
        }
      });

    this.store.select(authSelectors.verifyCode)
      .pipe(
        takeUntil(this.ngUnsubscribe)
      )
      .subscribe(data => {
        if (data) {
          this.isCodeFormSubmitted = true;
          this.sessionToken = data.sessionToken;
        }
      });

    this.store.select(authSelectors.registration)
      .pipe(
        takeUntil(this.ngUnsubscribe)
      )
      .subscribe(data => {
        if (data) {
          this.router.navigateByUrl(APP_URLS.login);
        }
      });
  }
}
