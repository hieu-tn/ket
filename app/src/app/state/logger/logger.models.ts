import { authActionTypes } from '@/state/auth/auth.actions';



export type loggerActionTypes = authActionTypes;

export interface ILoggerAction {
  action: loggerActionTypes
  payload?: any
}

export interface ILoggerState {
  loadings: Array<loggerActionTypes>
  errors: Array<ILoggerAction>
}
