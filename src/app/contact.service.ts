import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ContactService {

  uri = 'http://localhost:8000/contacts';

  constructor(private http: HttpClient) { }

  addContact(person_name, contact_name, contact_gst_number) {
    const obj = {
      person_name: person_name,
      contact_name: contact_name,
      contact_gst_number: contact_gst_number
    };
    console.log(obj);
    return this.http.post(`${this.uri}`, obj);
  }
  getContacts() {
    return this
           .http
           .get(`${this.uri}`);
  }

  editContact(id) {
    return this
          .http
          .get(`${this.uri}?id=${id}`);
  }
  updateContact(person_name, contact_name, contact_gst_number, id) {
    const obj = {
        id: id,
        person_name: person_name,
        contact_name: contact_name,
        contact_gst_number: contact_gst_number
      };
    return this
              .http
              .put(`${this.uri}`, obj);
  }
  deleteContact(id) {
    return this
              .http
              .request('delete',`${this.uri}`,{body: {id: id}});
  }
  viewContact(id) {
    return this
          .http
          .get(`${this.uri}/edit/${id}`);
  }
}