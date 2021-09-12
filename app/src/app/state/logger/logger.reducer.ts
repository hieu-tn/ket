import { createReducer, on } from '@ngrx/store';

import { ILoggerAction, ILoggerState, loggerActionTypes } from './logger.models';
import * as authActions from '@/state/auth/auth.actions';



export const initialState: ILoggerState = {
  loadings: [],
  errors: [],
};


export const loggerReducer = createReducer(
  initialState,
  on(authActions.login, (state, payload) => addLoadingActionToState(state, authActions.login.type)),
  on(authActions.loginSuccess, state => removeLoadingActionFromState(state, authActions.login.type)),
  on(authActions.loginFailure, (state, payload) => addErrorActionToState(state, {
    action: authActions.login.type, payload
  })),
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
