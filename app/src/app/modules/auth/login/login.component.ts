import { Component, OnDestroy, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { Store } from '@ngrx/store';
import { Subject } from 'rxjs';

import { formControlError } from '@/modules/shared/validators/form.validators';
import { ILoginPayloadAction } from '@/state/auth/auth.models';
import { IAppState } from '@/state/state.models';
import * as authActions from '@/state/auth/auth.actions';


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit, OnDestroy {

  loginForm: FormGroup = new FormGroup({});
  formControlError = formControlError;
  hidePassword: boolean = true;

  private ngUnsubscribe = new Subject();

  constructor(private store: Store<IAppState>) { }

  ngOnInit(): void {
    this.clearActions();
    this.initForms();
  }

  ngOnDestroy(): void {
    this.ngUnsubscribe.next();
    this.ngUnsubscribe.complete();
    this.clearActions();
  }

  onLoginFormSubmit(): void {
    if (this.loginForm.invalid) return;

    this.store.dispatch(authActions.login({...this.loginForm.value} as ILoginPayloadAction));
  }

  private initForms(): void {
    this.loginForm = new FormGroup({
      username: new FormControl('', [Validators.required]),
      password: new FormControl('', [Validators.required])
    });
  }

  private clearActions(): void {
    this.store.dispatch(authActions.clearLogin());
  }
}
