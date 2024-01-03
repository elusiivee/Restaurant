from django import forms
from .models import ContactMessage
class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    subject = forms.CharField(100)
    message = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = ContactMessage