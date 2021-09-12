import { Component, OnDestroy, OnInit } from '@angular/core';
import { Store } from '@ngrx/store';

import { IAppState } from '@/state/state.models';
import { authSelectors } from '@/state/auth/auth.selectors';
import * as authActions from '@/state/auth/auth.actions';


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit, OnDestroy {

  constructor(private store: Store<IAppState>) { }

  ngOnInit(): void {
    this.store.dispatch(authActions.login({
      password: '', username: ''
    }));
  }

  ngOnDestroy(): void {}

}
