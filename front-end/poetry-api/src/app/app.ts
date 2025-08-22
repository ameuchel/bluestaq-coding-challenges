import { throwError, catchError } from 'rxjs';
import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpErrorResponse } from '@angular/common/http';
import { PoetryService } from './poetry-search';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './app.html'
})
export class App {
  titleQuery = '';
  authorQuery = '';
  result = '';
  errorMessage = '';

  constructor(private poetryService: PoetryService) {}

  searchAuthor() {
    this.errorMessage = '';
    this.result = '';
    this.titleQuery = '';
    this.poetryService.searchAuthor(this.authorQuery)
      .pipe(
          catchError((error: HttpErrorResponse) => {
            if (error.status !== 200) {
              this.errorMessage = `API ERROR: ${error.status}: ${error.statusText}`;
              return throwError(() => new Error(this.errorMessage));
            }
            return throwError(() => new Error(this.errorMessage));
          })
        )
      .subscribe(data => {
        if (data.status && data.status !== 200) {
          this.errorMessage = `API ERROR: ${data.reason}`;
        }
        else {
          this.result = JSON.stringify(data).substring(0, 1000);
          console.log(data);
        }
      });
  }

  searchTitle() {
    this.errorMessage = '';
    this.result = '';
    this.authorQuery = '';
    this.poetryService.searchTitle(this.titleQuery)
      .pipe(
          catchError((error: HttpErrorResponse) => {
            if (error.status !== 200) {
              this.errorMessage = `API ERROR: ${error.status}: ${error.statusText}`;
              return throwError(() => new Error(this.errorMessage));
            }
            return throwError(() => new Error(this.errorMessage));
          })
        )
      .subscribe(data => {
        if (data.status && data.status !== 200) {
          this.errorMessage = `API ERROR: ${data.reason}`;
        }
        else {
          this.result = JSON.stringify(data).substring(0, 1000);
          console.log(data);
        }
      });
  }

}