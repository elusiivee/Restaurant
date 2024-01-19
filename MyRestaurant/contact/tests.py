from django.test import TestCase

from .forms import ContactForm
from .models import ContactInfo


class ContactFormTest(TestCase):
    '''
    Class for testing forms from ContactForm.
    '''

    def test_valid_data(self):
        form = ContactForm(data={
            'name': 'Mr Test',
            'email': 'test@gmail.com',
            'subject': 'testing',
            'message': 'i hope it will work!!!',
        })
        self.assertTrue(form.is_valid())

    def test_invalid_data(self):
        form = ContactForm(data={
            'name': 'Mr Test',
            'email': 'invalid',
            'subject': 'invalid',
            'message': 'invalid',
        })
        self.assertFalse(form.is_valid())
        print(form.errors)  # Print the form errors


class ContactInfoTest(TestCase):
    '''
    Class ContactInfoTest testing model ContactInfo

    Methods:
        setUp(self): Creates a sample contact_info item for testing.

        test_contact_info_item_attributes(self): Tests the attributes of the contact_info item created in setUp.
    '''

    def setUp(self):
        ContactInfo.objects.create(address='Item1', phone='12341232', email='test@gmail.com')

    def test_contact_info_item_attributes(self):
        contact_info = ContactInfo.objects.get(address="Item1")

        self.assertEqual(contact_info.address, "Item1")
        self.assertEqual(contact_info.phone, '12341232')
        self.assertEqual(contact_info.email, 'test@gmail.com')
