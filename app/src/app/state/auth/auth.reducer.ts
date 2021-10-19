import { createReducer, on } from '@ngrx/store';

import { IAuthState } from './auth.models';
import * as authActions from './auth.actions';


export const initialState: IAuthState = {
  verification: null,
  verifyCode: null,
  registration: null,
  login: null,
};

export const authReducer = createReducer(
  initialState,
  // getVerification
  on(
    authActions.getVerificationSuccess,
    (state, action) => ({...state, verification: action.payload})
  ),
  on(
    authActions.clearGetVerification,
    (state) => ({...state, verification: null})
  ),
  // getVerification
  // verifyCode
  on(
    authActions.verifyCodeSuccess,
    (state, action) => ({...state, verifyCode: action.payload})
  ),
  on(
    authActions.clearVerifyCode,
    (state) => ({...state, verifyCode: null})
  ),
  // verifyCode
  // registration
  on(
    authActions.registrationSuccess,
    (state, action) => ({...state, registration: action.payload})
  ),
  on(
    authActions.clearRegistration,
    (state) => ({...state, registration: null})
  ),
  // registration
  // login
  on(
    authActions.loginSuccess,
    (state, action) => ({...state, login: action.payload})
  ),
  on(
    authActions.clearRegistration,
    (state) => ({...state, login: null})
  ),
  // login
);
