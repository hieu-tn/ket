import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ActionReducer, ActionReducerMap, MetaReducer, StoreModule } from '@ngrx/store';
import { EffectsModule } from '@ngrx/effects';
import { StoreDevtoolsModule } from '@ngrx/store-devtools';

import { environment } from '@/environments/environment';
import { IAppState } from '@/state/state.models';
import { authReducer } from '@/state/auth/auth.reducer';
import { loggerReducer } from '@/state/logger/logger.reducer';
import { AuthEffects } from '@/state/auth/auth.effects';



export const reducers: ActionReducerMap<IAppState> = {
  auth: authReducer,
  logger: loggerReducer,
};

export const effects = [AuthEffects];

// console.log all actions
export function debug(reducer: ActionReducer<any>): ActionReducer<any> {
  return function (state, action) {
    // console.log('state', state);
    // console.log('action', action);

    return reducer(state, action);
  };
}

export const metaReducers: MetaReducer<IAppState>[] = [debug];

@NgModule({
  declarations: [],
  imports: [
    CommonModule,
    StoreModule.forRoot(reducers, {metaReducers}),
    EffectsModule.forRoot(effects),
    StoreDevtoolsModule.instrument({name: 'KET NgRx Store DevTools', maxAge: 50, logOnly: environment.production}),
  ]
})
export class StateModule {}
