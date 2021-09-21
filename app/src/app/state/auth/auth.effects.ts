import { Injectable } from '@angular/core';
import { Actions, createEffect, ofType } from '@ngrx/effects';
import { authActionTypes } from './auth.actions';
import { map } from 'rxjs/operators';
import * as authActions from './auth.actions';


@Injectable()
export class AuthEffects {

  getVerification$ = createEffect(() => this.actions$.pipe(
    ofType(authActionTypes.getVerification),
    map(() => {
      return authActions.getVerificationSuccess(true);
    })
  ));

  verifyCode$ = createEffect(() => this.actions$.pipe(
    ofType(authActionTypes.verifyCode),
    map(() => {
      return authActions.verifyCodeSuccess({});
    })
  ));

  constructor(private actions$: Actions) {}

}
