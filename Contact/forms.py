from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']  # আপনার মডেলের ফিল্ডের নাম

        widgets = {
            'name': forms.TextInput(attrs={
                'name': 'contactName',
                'id': 'contactName',
                'placeholder': 'Name',
                'minlength': '2',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'name': 'contactEmail',
                'id': 'contactEmail',
                'placeholder': 'Email',
                'required': True
            }),
            'subject': forms.TextInput(attrs={
                'name': 'contactSubject',
                'id': 'contactSubject',
                'placeholder': 'Subject',
            }),
            'message': forms.Textarea(attrs={
                'name': 'contactMessage',
                'id': 'contactMessage',
                'placeholder': 'Message',
                'rows': '10',
                'cols': '50',
                'required': True
            }),
        }
