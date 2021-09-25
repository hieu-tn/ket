import { Injectable } from '@angular/core';
import { Actions, createEffect, ofType } from '@ngrx/effects';
import { authActionTypes } from './auth.actions';
import { catchError, map, switchMap } from 'rxjs/operators';
import { of } from 'rxjs';
import { TranslateService } from '@ngx-translate/core';
import * as authActions from './auth.actions';
import { NotificationService } from '@/services/notification.service';
import { AuthService } from '@/modules/auth/auth.service';
import {
  IGetVerificationPayloadAction,
  IRegistrationPayloadAction,
  IVerifyCodePayloadAction
} from '@/state/auth/auth.models';


@Injectable()
export class AuthEffects {

  getVerification$ = createEffect(() => this.actions$.pipe(
    ofType(authActionTypes.getVerification),
    switchMap(({payload}: {payload: IGetVerificationPayloadAction}) => {
      return this.authService.getVerification$(payload.authType, payload.target)
        .pipe(
          map(response => {
            this.notificationService.success(this.translateService.instant('common.notifications.verification.success'));
            return authActions.getVerificationSuccess(response);
          }),
          catchError((err: any) => {
            this.notificationService.error(this.translateService.instant('common.notifications.verification.failure'));
            return of(authActions.getVerificationFailure(err));
          })
        );
    })
  ));

  verifyCode$ = createEffect(() => this.actions$.pipe(
    ofType(authActionTypes.verifyCode),
    switchMap(({payload}: {payload: IVerifyCodePayloadAction}) => {
      return this.authService.verifyCode$(payload.sessionToken, payload.code)
        .pipe(
          map(response => {
            this.notificationService.success(this.translateService.instant('common.notifications.verifyCode.success'));
            return authActions.verifyCodeSuccess(response);
          }),
          catchError(err => {
            this.notificationService.error(this.translateService.instant('common.notifications.verifyCode.failure'));
            return of(authActions.getVerificationFailure(err));
          })
        );
    })
  ));

  register$ = createEffect(() => this.actions$.pipe(
    ofType(authActionTypes.registration),
    switchMap(({payload}: {payload: IRegistrationPayloadAction}) => {
      return this.authService.register$(payload.sessionToken, payload.password)
        .pipe(
          map(response => {
            this.notificationService.success(this.translateService.instant('common.notifications.registration.success'));
            return authActions.registrationSuccess(response);
          }),
          catchError(err => {
            this.notificationService.error(this.translateService.instant('common.notifications.registration.failure'));
            return of(authActions.registrationFailure(err));
          })
        );
    })
  ));

  constructor(private actions$: Actions,
              private notificationService: NotificationService,
              private authService: AuthService,
              private translateService: TranslateService) {}

}
