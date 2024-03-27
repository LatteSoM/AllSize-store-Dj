from django import forms
import re


class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=100, required=True)
    phone_number = forms.CharField(label='Номер телефона', max_length=18, required=True)

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if not re.match(r'^\+7\d{3}\d{3}\d{2}\d{2}$', phone_number):
            raise forms.ValidationError('Номер телефона должен быть в формате +7 (XXX) XXX-XX-XX')
        return phone_number
