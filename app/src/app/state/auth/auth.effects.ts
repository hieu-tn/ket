import { Injectable } from '@angular/core';
import { Actions, createEffect, ofType } from '@ngrx/effects';
import { authActionTypes } from './auth.actions';
import { map } from 'rxjs/operators';
import { of } from 'rxjs';
import * as authActions from './auth.actions'



@Injectable()
export class AuthEffects {

  login$ = createEffect(() => this.actions$.pipe(
    ofType(authActionTypes.login),
    map(() => {
      return authActions.loginSuccess({
        challenge: ''
      });
    })
  ));


  constructor(private actions$: Actions) {}

}
