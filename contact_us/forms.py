from django import forms


class contact_form(forms.Form):
    full_name = forms.CharField(max_length=200)
    email = forms.CharField(max_length=200)
    designation = forms.CharField(max_length=400)
    company_name = forms.CharField(max_length=400)
    phone_number = forms.CharField(max_length=13)
    note = forms.CharField(max_length = 1000,)