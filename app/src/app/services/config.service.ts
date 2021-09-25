import { Injectable } from '@angular/core';

import { environment } from '@/environments/environment';


export const configServiceProvider = () => {
  const config = new ConfigService();
  let env = environment;

  Object.entries(env).map(([k, v]) => {
    if (config.hasOwnProperty(k)) Object.assign(config, {[k]: v});
  });

  return config;
};

@Injectable({
  providedIn: 'root'
})
export class ConfigService {
  public production: string = '';
  public apiUrl: string = '';

  constructor() { }
}
