import { createSelector } from '@ngrx/store';

import { IAppState } from '@/state/state.models';
import { IAuthState } from './auth.models';



const state = (state: IAppState) => state.auth;

export const authSelectors = {
  verification: createSelector(state, (state: IAuthState) => state.verification),
  verifyCode: createSelector(state, (state: IAuthState) => state.verifyCode),
  registration: createSelector(state, (state: IAuthState) => state.registration),
};
