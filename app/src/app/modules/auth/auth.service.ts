import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { AuthTypes } from './auth.models';
import { Observable, of } from 'rxjs';
import { ConfigService } from '@/services/config.service';
import { map } from 'rxjs/operators';


@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor(private httpClient: HttpClient, private configService: ConfigService) { }

  getVerification$(authType: AuthTypes, target: string): Observable<any> {
    const body = {authType, target};
    return this.httpClient.post(this.configService.apiUrl + '/auth/verification/', body);
  }

  verifyCode$(sessionToken: string, code: string): Observable<any> {
    const body = {sessionToken, code};
    return this.httpClient.post(this.configService.apiUrl + '/auth/verification-check/', body);
  }

  register$(sessionToken: string, password: string): Observable<any> {
    const body = {sessionToken, password};
    return this.httpClient.post(this.configService.apiUrl + '/users/', body)
      .pipe(
        map(() => true)
      );
  }

  login$(username: string, password: string): Observable<any> {
    const body = {username, password};
    return this.httpClient.post(this.configService.apiUrl + '/auth/', body);
  }
}
