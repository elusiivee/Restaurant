from django.test import TestCase

from .forms import ReservationForm


class ReservationFormTest(TestCase):
    '''
    Class for testing forms from ReservationForm.
    '''

    def test_valid_data(self):
        form = ReservationForm(data={
            'name': 'Mr Test',
            'email': 'test@gmail.com',
            'phone': '124124124',
            'date': '2023-10-10',
            'time': '17:00',
            'people': '2',
        })
        self.assertTrue(form.is_valid())

    def test_invalid_data(self):
        form = ReservationForm(data={
            'name': 'Mr Test',
            'email': 'invalid',
            'phone': 'invalid',
            'date': 'invalid',
            'time': 'invalid',
            'people': 'invalid',
        })
        self.assertFalse(form.is_valid())
        print(form.errors)  # Print the form errors
