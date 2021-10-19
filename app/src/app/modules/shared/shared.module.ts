import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { MatButtonModule } from '@angular/material/button';
import { MatSnackBarModule } from '@angular/material/snack-bar';
import { ReactiveFormsModule } from '@angular/forms';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatSelectModule } from '@angular/material/select';
import { MatIconModule } from '@angular/material/icon';
import { OverlayModule } from '@angular/cdk/overlay';
import { MatInputModule } from '@angular/material/input';
import { MatStepperModule } from '@angular/material/stepper';

import { HeaderComponent } from './components/header/header.component';
import { FooterComponent } from './components/footer/footer.component';
import { DefaultLayoutComponent } from './layouts/default/default.component';
import { TranslationModule } from './translation/translation.module';
import { CapitalizePipe } from './pipes/capitalize.pipe';


@NgModule({
  declarations: [
    HeaderComponent,
    FooterComponent,
    DefaultLayoutComponent,
    CapitalizePipe,
  ],
  imports: [
    CommonModule,
    RouterModule,
    TranslationModule,
    MatSnackBarModule,
    ReactiveFormsModule,
    MatFormFieldModule,
    MatSelectModule,
    MatIconModule,
    OverlayModule,
    MatInputModule,
    MatButtonModule,
    MatStepperModule,
  ],
  exports: [
    TranslationModule,
    CapitalizePipe,
    MatSnackBarModule,
    ReactiveFormsModule,
    MatFormFieldModule,
    MatSelectModule,
    MatIconModule,
    OverlayModule,
    MatInputModule,
    MatButtonModule,
    MatStepperModule,
  ]
})
export class SharedModule {}
