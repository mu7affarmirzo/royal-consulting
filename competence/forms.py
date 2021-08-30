from django import forms
from phonenumber_field.modelfields import PhoneNumberField
from competence.models import ContactUsModel


class ContactUsForm(forms.ModelForm):

    class Meta:
        model = ContactUsModel
        fields = [
            'full_name',
            'message',
            'phone_number',
            'email',
        ]