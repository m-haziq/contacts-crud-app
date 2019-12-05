from django.test import TestCase
from rest_framework.test import APIClient
from .models import Contact


class ContactTests(TestCase):
    client = APIClient()

    # Validation Tests
    def test_add_invalid_name_field(self):
        body = {
            "person_name": 1,
            "contact_name": "TEST@TSET.COM",
            "contact_gst_number": "123467213123121231231231"
        }
        response = self.client.post('/contacts', body, format='json')
        self.assertEqual(response.status_code, 400)

    def test_add_invalid_phone_field(self):
        body = {
            "person_name": "TEST",
            "contact_name": "TEST@TSET.COM",
            "contact_gst_number": "123467213123121231231231"
        }
        response = self.client.post('/contacts', body, format='json')
        self.assertEqual(response.status_code, 400)

    def test_add_invalid_email_field(self):
        body = {
            "person_name": "TEST",
            "contact_name": "INVALIDEMAILVALUE",
            "contact_gst_number": "123467213123121231231231"
        }
        response = self.client.post('/contacts', body, format='json')
        self.assertEqual(response.status_code, 400)

    # CRUD tests
    def test_add_contact(self):
        body = {
            "person_name": "TEST",
            "contact_name": "TEST@TSET.COM",
            "contact_gst_number": "12346721"
        }
        response = self.client.post('/contacts', body, format='json')
        self.assertEqual(response.status_code, 201)

    def test_get_contacts(self):
        for _ in range(10):
            contact = Contact(
                person_name=f'test{_ + 1}',
                contact_name=f'test{_ + 1}@test.com',
                contact_gst_number=f'123465-{_ + 1}'
            )
            contact.save()
        response = self.client.get('/contacts')
        self.assertEqual(len(response.data), 10)

    def test_get_target_contact(self):
        for _ in range(10):
            contact = Contact(
                id=_,
                person_name=f'test{_ + 1}',
                contact_name=f'test{_ + 1}@test.com',
                contact_gst_number=f'123465-{_ + 1}'
            )
            contact.save()
        response = self.client.get(
            f'/contacts?id={5}'
        )
        self.assertEqual(response.data[0]['id'], 5)

    def test_update_contact(self):
        contact = Contact(
            person_name='test',
            contact_name='test@test.com',
            contact_gst_number='1234656'
        )
        contact.save()
        response = self.client.put(
            '/contacts',
            data={"id": contact.id, "person_name": "test-done"},
            content_type='application/json'
        )
        print(response.data)
        self.assertEqual(response.data['person_name'], 'test-done')

    def test_del_contact(self):
        for _ in range(5):
            contact = Contact(
                person_name=f'test{_ + 1}',
                contact_name=f'test{_ + 1}@test.com',
                contact_gst_number=f'123465-{_ + 1}'
            )
            contact.save()
        response = self.client.delete(
            '/contacts',
            data={"id": contact.id},
            content_type='application/json')
        self.assertEqual(len(response.data), 4)
