from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())

    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 3, 'placeholder': 'Message'}
        ),
        max_length=300,
        help_text='Max 300 characters.',
        required=True
    )

    class Meta:
        model = Contact
        fields = ('name', 'email', 'message',)
