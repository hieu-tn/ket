import { Injectable } from '@angular/core';


@Injectable({
  providedIn: 'root'
})
export class LoggingService {

  constructor() { }

  public info(value: any): void {
    console.log(value);
  }

  public error(value: any): void {
    console.log('ERROR', value);
  }

  public warning(value: any): void {
    console.log('WARNING', value);
  }
}
