import { createReducer, on } from '@ngrx/store';

import { ILoggerAction, ILoggerState, loggerActionTypes } from './logger.models';
import * as authActions from '@/state/auth/auth.actions';
import { authActionTypes } from '@/state/auth/auth.actions';


export const initialState: ILoggerState = {
  loadings: [],
  errors: [],
};


export const loggerReducer = createReducer(
  initialState,
  // getVerification
  on(
    authActions.getVerification,
    state => addLoadingActionToState(state, authActionTypes.getVerification)
  ),
  on(
    authActions.getVerificationSuccess,
    state => removeLoadingActionFromState(state, authActionTypes.getVerification)
  ),
  on(
    authActions.getVerificationFailure,
    (state, data) => addErrorActionToState(state, {
      action: authActionTypes.getVerification, payload: data.payload
    })
  ),
  on(
    authActions.clearGetVerification,
    (state) => clearActionFromState(state, authActionTypes.getVerification),
  ),
  // getVerification
  // verifyCode
  on(
    authActions.verifyCode,
    state => addLoadingActionToState(state, authActionTypes.verifyCode)
  ),
  on(
    authActions.verifyCodeSuccess,
    state => removeLoadingActionFromState(state, authActionTypes.verifyCode)
  ),
  on(
    authActions.verifyCodeFailure,
    (state, data) => addErrorActionToState(state, {
      action: authActionTypes.verifyCode, payload: data.payload
    })
  ),
  on(
    authActions.clearVerifyCode,
    (state) => clearActionFromState(state, authActionTypes.verifyCode),
  ),
  // verifyCode
  // registration
  on(
    authActions.registration,
    state => addLoadingActionToState(state, authActionTypes.registration)
  ),
  on(
    authActions.registrationSuccess,
    state => removeLoadingActionFromState(state, authActionTypes.registration)
  ),
  on(
    authActions.registrationFailure,
    (state, data) => addErrorActionToState(state, {
      action: authActionTypes.registration, payload: data.payload
    })
  ),
  on(
    authActions.clearRegistration,
    (state) => clearActionFromState(state, authActionTypes.registration),
  ),
  // registration
  // login
  on(
    authActions.login,
    state => addLoadingActionToState(state, authActionTypes.login)
  ),
  on(
    authActions.loginSuccess,
    state => removeLoadingActionFromState(state, authActionTypes.login)
  ),
  on(
    authActions.loginFailure,
    (state, data) => addErrorActionToState(state, {
      action: authActionTypes.login, payload: data.payload
    })
  ),
  on(
    authActions.clearLogin,
    (state) => clearActionFromState(state, authActionTypes.login),
  ),
  // login
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

const clearActionFromState = (state: ILoggerState, action: loggerActionTypes): ILoggerState => {
  return {
    ...state,
    loadings: state.loadings.filter(a => a !== action),
    errors: state.errors.filter(a => a.action !== action),
  };
};
