import { Injectable } from '@angular/core';
import { Actions, createEffect, ofType } from '@ngrx/effects';
import { catchError, map, switchMap } from 'rxjs/operators';
import { of } from 'rxjs';
import { TranslateService } from '@ngx-translate/core';

import * as authActions from './auth.actions';
import { NotificationService } from '@/services/notification.service';
import { AuthService } from '@/modules/auth/auth.service';
import {
  IGetVerificationPayloadAction, ILoginPayloadAction,
  IRegistrationPayloadAction,
  IVerifyCodePayloadAction
} from '@/state/auth/auth.models';


@Injectable()
export class AuthEffects {

  getVerification$ = createEffect(() => this.actions$.pipe(
    ofType(authActions.authActionTypes.getVerification),
    switchMap((action: {type: authActions.authActionTypes, payload: IGetVerificationPayloadAction}) => {
      return this.authService.getVerification$(action.payload.authType, action.payload.target)
        .pipe(
          map(response => {
            this.notificationService.actionSuccess(action.type);
            return authActions.getVerificationSuccess(response);
          }),
          catchError((err: any) => {
            this.notificationService.actionFailure(action.type);
            return of(authActions.getVerificationFailure(err));
          })
        );
    })
  ));

  verifyCode$ = createEffect(() => this.actions$.pipe(
    ofType(authActions.authActionTypes.verifyCode),
    switchMap((action: {type: authActions.authActionTypes, payload: IVerifyCodePayloadAction}) => {
      return this.authService.verifyCode$(action.payload.sessionToken, action.payload.code)
        .pipe(
          map(response => {
            this.notificationService.actionSuccess(action.type);
            return authActions.verifyCodeSuccess(response);
          }),
          catchError(err => {
            this.notificationService.actionFailure(action.type);
            return of(authActions.getVerificationFailure(err));
          })
        );
    })
  ));

  register$ = createEffect(() => this.actions$.pipe(
    ofType(authActions.authActionTypes.registration),
    switchMap((action: {type: authActions.authActionTypes, payload: IRegistrationPayloadAction}) => {
      return this.authService.register$(action.payload.sessionToken, action.payload.password)
        .pipe(
          map(response => {
            this.notificationService.actionSuccess(action.type);
            return authActions.registrationSuccess(response);
          }),
          catchError(err => {
            this.notificationService.actionFailure(action.type);
            return of(authActions.registrationFailure(err));
          })
        );
    })
  ));

  login$ = createEffect(() => this.actions$.pipe(
    ofType(authActions.authActionTypes.login),
    switchMap((action: {type: authActions.authActionTypes, payload: ILoginPayloadAction}) => {
      return this.authService.login$(action.payload.username, action.payload.password)
        .pipe(
          map(response => {
            this.notificationService.actionSuccess(action.type);
            return authActions.loginSuccess(response);
          }),
          catchError(err => {
            this.notificationService.actionFailure(action.type);
            return of(authActions.loginFailure(err));
          })
        )
    })
  ))

  constructor(private actions$: Actions,
              private notificationService: NotificationService,
              private authService: AuthService,
              private translateService: TranslateService) {}

}
