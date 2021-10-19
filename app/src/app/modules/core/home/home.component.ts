import { Component, OnInit } from '@angular/core';

import { APP_URLS } from '@/constants/urls';


@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

  APP_URLS = APP_URLS;

  constructor() { }

  ngOnInit(): void {
  }

}
