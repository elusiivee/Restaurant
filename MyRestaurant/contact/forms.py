from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    '''
    Form for handling contact messages.

    Attributes:
        name (CharField): Input field for the sender's name.
        email (EmailField): Input field for the sender's email address.
        subject (CharField): Input field for the subject of the contact message.
        message (CharField): Input field for the content of the contact message.

    Meta:
        model (ContactMessage): Specifies the model associated with the form.
        fields (list): List of fields to include in the form.
    '''

    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']

    name = forms.CharField(
        max_length=200,
        label='Your Name',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'})
    )
    email = forms.EmailField(
        label='Your Email',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'})
    )
    subject = forms.CharField(
        max_length=100,
        label='Subject',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'})
    )
    message = forms.CharField(
        max_length=255,
        label='Message',
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message'})
    )
