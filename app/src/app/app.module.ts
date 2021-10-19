import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { OverlayModule } from '@angular/cdk/overlay';
import { TranslateLoader, TranslateModule } from '@ngx-translate/core';
import { HttpClient } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

import { StateModule } from '@/state/state.module';
import { SharedModule } from '@/modules/shared/shared.module';
import { createTranslateLoader } from '@/modules/shared/translation/translation.module';
import { ConfigService, configServiceProvider } from '@/services/config.service';


@NgModule({
  declarations: [
    AppComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    StateModule,
    SharedModule,
    OverlayModule,
    TranslateModule.forRoot({
      loader: {
        provide: TranslateLoader,
        useFactory: (createTranslateLoader),
        deps: [HttpClient]
      },
      defaultLanguage: 'en'
    })
  ],
  providers: [
    {
      provide: ConfigService,
      useFactory: (configServiceProvider),
      deps: []
    }
  ],
  bootstrap: [AppComponent],
})
export class AppModule {}
