from .models import Contact
from django import forms


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('name', 'phone', 'designation', 'image', 'email')
