from django import forms
from . models import Contact
class ContactForm(forms.ModelsForm):
    class Meta:
        model=Contact
        fields=['name','email','message']
    
    def clean_mesage(self):
        message=self.cleaned_data.get('message')
        if len(message)<10:
            raise forms.validationError('message must be at least 10 characters')
        return message

class FeedbackForm(forms.ModelsForm):
    class Meta:
        models=Feedback
        fields='_all_'