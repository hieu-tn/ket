import { createAction, props } from '@ngrx/store';
import {
  IGetVerificationPayloadAction, ILoginPayloadAction,
  IRegistrationPayloadAction, IVerification,
  IVerifyCode,
  IVerifyCodePayloadAction
} from './auth.models';


export enum authActionTypes {
  getVerification = '[Auth] Get Verification',
  getVerificationSuccess = '[Auth] Get Verification Success',
  getVerificationFailure = '[Auth] Get Verification Failure',
  clearGetVerification = '[Auth] Clear Get Verification',

  verifyCode = '[Auth] Verify code',
  verifyCodeSuccess = '[Auth] Verify code Success',
  verifyCodeFailure = '[Auth] Verify code Failure',
  clearVerifyCode = '[Auth] Clear Verify code',

  registration = '[Auth] Registration',
  registrationSuccess = '[Auth] Registration Success',
  registrationFailure = '[Auth] Registration Failure',
  clearRegistration = '[Auth] Clear Registration',

  login = '[Auth] Login',
  loginSuccess = '[Auth] Login Success',
  loginFailure = '[Auth] Login Failure',
  clearLogin = '[Auth] Clear Login',
}

// getVerification
export const getVerification = createAction(
  authActionTypes.getVerification,
  (payload: IGetVerificationPayloadAction) => ({payload}),
);
export const getVerificationSuccess = createAction(
  authActionTypes.getVerificationSuccess,
  (payload: IVerification) => ({payload}),
);
export const getVerificationFailure = createAction(
  authActionTypes.getVerificationFailure,
  (payload: any) => ({payload}),
);
export const clearGetVerification = createAction(
  authActionTypes.clearGetVerification,
  (payload: any = null) => ({payload}),
);
// getVerification

// verifyCode
export const verifyCode = createAction(
  authActionTypes.verifyCode,
  (payload: IVerifyCodePayloadAction) => ({payload})
);
export const verifyCodeSuccess = createAction(
  authActionTypes.verifyCodeSuccess,
  (payload: IVerifyCode) => ({payload})
);
export const verifyCodeFailure = createAction(
  authActionTypes.verifyCodeFailure,
  (payload: any) => ({payload})
);
export const clearVerifyCode = createAction(
  authActionTypes.clearVerifyCode,
  (payload: any = null) => ({payload}),
);
// verifyCode

// registration
export const registration = createAction(
  authActionTypes.registration,
  (payload: IRegistrationPayloadAction) => ({payload})
);
export const registrationSuccess = createAction(
  authActionTypes.registrationSuccess,
  (payload: any) => ({payload})
);
export const registrationFailure = createAction(
  authActionTypes.registrationFailure,
  (payload: any) => ({payload})
);
export const clearRegistration = createAction(
  authActionTypes.clearRegistration,
  (payload: any = null) => ({payload}),
);
// registration

// login
export const login = createAction(
  authActionTypes.login,
  (payload: ILoginPayloadAction) => ({payload})
);
export const loginSuccess = createAction(
  authActionTypes.loginSuccess,
  (payload: any) => ({payload})
);
export const loginFailure = createAction(
  authActionTypes.loginFailure,
  (payload: any) => ({payload})
);
export const clearLogin = createAction(
  authActionTypes.clearLogin,
  (payload: any = null) => ({payload}),
);
// login
