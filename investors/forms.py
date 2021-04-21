from django import forms
from django_countries.widgets import CountrySelectWidget
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from investors.models import UserApplication

class InvestorForm(forms.Form):
    country = CountryField(blank_label="Select country").formfield(widget=CountrySelectWidget(attrs={
        "class": "my_input_form"
    }))
    full_name = forms.CharField()
    company_name = forms.CharField()
    postion = forms.CharField()
    number = PhoneNumberField()
    email = forms.EmailField()
    investment_value = forms.CharField()
    message = forms.Textarea()



class CreateBlogPostForm(forms.ModelForm):
    # country = CountryField(blank_label="Select country").formfield(widget=CountrySelectWidget(attrs={
    #     "class": "my_input_form"
    # }))
    class Meta:
        model = UserApplication
        fields = [
            # 'country',
            'company_name',
            'full_name',
            'postion',
            'number',
            'email',
            'investment_value',
            'message',
        ]