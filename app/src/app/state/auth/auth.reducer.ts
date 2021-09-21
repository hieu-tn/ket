import { createReducer, on } from '@ngrx/store';

import { IAuthState } from './auth.models';
import * as authActions from './auth.actions';


export const initialState: IAuthState = {
  verification: null,
  verifyCode: null,
  registration: null,
};

export const authReducer = createReducer(
  initialState,
  on(
    authActions.getVerificationSuccess,
    (state, data) => ({...state, verification: data.payload})
  ),
  on(
    authActions.verifyCodeSuccess,
    (state, data) => ({...state, verifyCode: data.payload})
  ),
  on(
    authActions.registrationSuccess,
    (state, data) => ({...state, registration: data.payload})
  ),
);
