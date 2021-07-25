from django import forms
from django.contrib.auth.models import User
from django.core import validators


class UserNewOrderForm(forms.Form):
    product_id = forms.IntegerField(
        widget=forms.HiddenInput()
    )

    count = forms.IntegerField(
        widget=forms.NumberInput(attrs={'min': '1', 'class': 'form-control input-number'}),
        initial=1
    )
