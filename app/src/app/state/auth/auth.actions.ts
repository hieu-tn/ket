import { createAction, props } from '@ngrx/store';
import {
  IGetVerificationPayloadAction,
  IRegistrationPayloadAction, IVerification,
  IVerifyCode,
  IVerifyCodePayloadAction
} from './auth.models';


export enum authActionTypes {
  getVerification = '[Auth] Get Verification',
  getVerificationSuccess = '[Auth] Get Verification Success',
  getVerificationFailure = '[Auth] Get Verification Failure',

  verifyCode = '[Auth] Verify code',
  verifyCodeSuccess = '[Auth] Verify code Success',
  verifyCodeFailure = '[Auth] Verify code Failure',

  registration = '[Auth] Registration',
  registrationSuccess = '[Auth] Registration Success',
  registrationFailure = '[Auth] Registration Failure',
}

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
