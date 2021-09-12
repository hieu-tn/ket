import { createReducer, on } from '@ngrx/store';

import { IAuthState } from './auth.models';
import { login } from './auth.actions';



export const initialState: IAuthState = {};

export const authReducer = createReducer(
  initialState,
);
