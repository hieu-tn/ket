import { Injectable } from '@angular/core';
import { MatSnackBar } from '@angular/material/snack-bar';

import { NOTIFICATION_LIFETIME } from '@/constants/common';


@Injectable({
  providedIn: 'root'
})
export class NotificationService {

  private btnText: string = 'Close';

  constructor(private _snackBar: MatSnackBar) { }

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
}
