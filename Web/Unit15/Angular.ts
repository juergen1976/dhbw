import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app',
  template: `
    <h1>Data</h1>
    <ul>
      <li *ngFor="let item of data">{{ item.name }}</li>
    </ul>
  `
})
export class App {
  data = [];

  constructor(private http: HttpClient) { }

  ngOnInit() {
    this.http.get('https://api.example.com/data')
      .subscribe(response => this.data = response.data);
  }
}