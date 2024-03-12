from django import forms
from .models import reader

class ReaderForm(forms.ModelForm):
    class Meta:
        model = reader
        fields = ['reader_name', 'reference_id', 'reader_contact', 'reader_address']
        widgets = {
            'reader_address': forms.Textarea(attrs={'class': 'form-control'}),
        }
        error_messages = {
            'reader_name': {
                'min_length': "Minimum 3 characters required.",
            },
            'reader_contact': {
                'min_length': "Minimum 10 digits required.",
            }
        }

    def clean_reader_name(self):
        name = self.cleaned_data.get('reader_name')
        if len(name) < 3:
            raise forms.ValidationError("Minimum 3 characters required.")
        return name

    def clean_reader_contact(self):
        contact = self.cleaned_data.get('reader_contact')
        if len(contact) < 10:
            raise forms.ValidationError("Minimum 10 digits required.")
        return contact
