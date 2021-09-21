import { createReducer, on } from '@ngrx/store';

import { ILoggerAction, ILoggerState, loggerActionTypes } from './logger.models';
import * as authActions from '@/state/auth/auth.actions';


export const initialState: ILoggerState = {
  loadings: [],
  errors: [],
};


export const loggerReducer = createReducer(
  initialState,
  on(
    authActions.getVerification,
    state => addLoadingActionToState(state, authActions.getVerification.type)
  ),
  on(
    authActions.getVerificationSuccess,
    state => removeLoadingActionFromState(state, authActions.getVerification.type)
  ),
  on(
    authActions.getVerificationFailure,
    (state, data) => addErrorActionToState(state, {
      action: authActions.getVerification.type, payload: data.payload
    })
  ),
  on(
    authActions.verifyCode,
    state => addLoadingActionToState(state, authActions.verifyCode.type)
  ),
  on(
    authActions.verifyCodeSuccess,
    state => removeLoadingActionFromState(state, authActions.verifyCode.type)
  ),
  on(
    authActions.verifyCodeFailure,
    (state, data) => addErrorActionToState(state, {
      action: authActions.verifyCode.type, payload: data.payload
    })
  ),
  on(
    authActions.registration,
    state => addLoadingActionToState(state, authActions.registration.type)
  ),
  on(
    authActions.registrationSuccess,
    state => removeLoadingActionFromState(state, authActions.registration.type)
  ),
  on(
    authActions.registrationFailure,
    (state, data) => addErrorActionToState(state, {
      action: authActions.registration.type, payload: data.payload
    })
  ),
);

const addLoadingActionToState = (state: ILoggerState, action: loggerActionTypes): ILoggerState => {
  return {...state, loadings: [...state.loadings, action]};
};

const addErrorActionToState = (state: ILoggerState, action: ILoggerAction): ILoggerState => {
  return {...state, errors: [...state.errors, action]};
};

const removeLoadingActionFromState = (state: ILoggerState, action: loggerActionTypes): ILoggerState => {
  return {...state, loadings: state.loadings.filter(a => a !== action)};
};
