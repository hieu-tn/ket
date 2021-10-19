import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { DefaultLayoutComponent } from '@/modules/shared/layouts/default/default.component';
import { RegistrationComponent } from '@/modules/auth/registration/registration.component';
import { LoginComponent } from '@/modules/auth/login/login.component';
import { HomeComponent } from '@/modules/core/home/home.component';
import { DashboardComponent } from '@/modules/dashboard/dashboard.component';


const routes: Routes = [
  {
    path: '',
    component: DefaultLayoutComponent,
    children: [
      {
        path: '',
        component: HomeComponent,
      },
      {
        path: 'registration',
        component: RegistrationComponent
      },
      {
        path: 'login',
        component: LoginComponent
      },
      {
        path: 'dashboard',
        component: DashboardComponent
      },
    ]
  },
  {
    path: '',
    pathMatch: 'full',
    loadChildren: () => import('@/modules/core/home/home.module').then(m => m.HomeModule)
  },
  {
    path: 'registration',
    loadChildren: () => import('@/modules/auth/registration/registration.module').then(m => m.RegistrationModule)
  },
  {
    path: 'login',
    loadChildren: () => import('@/modules/auth/login/login.module').then(m => m.LoginModule)
  },
  {
    path: 'dashboard',
    loadChildren: () => import('@/modules/dashboard/dashboard.module').then(m => m.DashboardModule)
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
