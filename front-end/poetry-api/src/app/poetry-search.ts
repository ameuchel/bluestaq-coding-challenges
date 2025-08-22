import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({ providedIn: 'root' })
export class PoetryService {
  constructor(private http: HttpClient) {}

  searchAuthor(query: string) {
    return this.http.get<any>(`https://poetrydb.org/author/${query}/author,title`);
  }

  searchTitle(query: string) {
    return this.http.get<any>(`https://poetrydb.org/title/${query}/author,title`);
  }

}