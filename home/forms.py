from django import forms
from . models import Contact
class ContactForm(forms.ModelsForm):
    class Meta:
        model=Contact
        fields=['name','email']