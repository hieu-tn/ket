import { createAction, props } from '@ngrx/store';
import {
  ILoginDispatchAction,
  ILoginSuccessDispatchAction,
} from './auth.models';



export enum authActionTypes {
  login = '[Auth] Login',
  loginSuccess = '[Auth] Login Success',
  loginFailure = '[Auth] Login Failure',
}

export const login = createAction(
  authActionTypes.login,
  (payload: ILoginDispatchAction) => ({payload}),
);

export const loginSuccess = createAction(
  authActionTypes.loginSuccess,
  (payload: ILoginSuccessDispatchAction) => ({payload}),
);

export const loginFailure = createAction(
  authActionTypes.loginFailure,
  props<any>()
);
