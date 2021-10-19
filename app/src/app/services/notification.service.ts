import { Injectable } from '@angular/core';
import { MatSnackBar } from '@angular/material/snack-bar';
import { TranslateService } from '@ngx-translate/core';

import { NOTIFICATION_LIFETIME } from '@/constants/common';


@Injectable({
  providedIn: 'root'
})
export class NotificationService {

  private btnText: string = 'Close';

  constructor(private _snackBar: MatSnackBar, private translateService: TranslateService) { }

  success(message: string): void {
    this._snackBar.open(message, this.btnText, {
      duration: NOTIFICATION_LIFETIME,
    });
  }

  error(message: string): void {
    this._snackBar.open(message, this.btnText, {
      duration: NOTIFICATION_LIFETIME,
    });
  }

  warning(message: string): void {
    this._snackBar.open(message, this.btnText, {
      duration: NOTIFICATION_LIFETIME,
    });
  }

  actionSuccess(type: string): void {
    const str = type + ' ' + this.translateService.instant('common.notifications.success');
    this.success(str);
  }

  actionFailure(type: string): void {
    const str = type + ' ' + this.translateService.instant('common.notifications.failure');
    this.error(str);
  }
}
