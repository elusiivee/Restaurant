from django.test import TestCase

from .forms import ContactForm


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
