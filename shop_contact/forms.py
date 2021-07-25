from django import forms
from django.core import validators


class CreateContactForm(forms.Form):
    full_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'نام', 'class': 'form-control'}),
        validators=[
            validators.MaxLengthValidator(150, 'تعداد کاراکتر ها نمی تواند بیش از 150 کاراکتر باشد')
        ]
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'ایمیل', 'class': 'form-control'}),
        validators=[
            validators.MaxLengthValidator(150, 'تعداد کاراکتر ها نمی تواند بیش از 150 کاراکتر باشد')
        ]
    )

    subject = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'موضوع', 'class': 'form-control'}),
        validators=[
            validators.MaxLengthValidator(150, 'تعداد کاراکتر ها نمی تواند بیش از 150 کاراکتر باشد')
        ]
    )

    text = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'متن پیام', 'class': 'form-control', 'cols': '30', 'rows': '7'}),
        validators=[
            validators.MaxLengthValidator(150, 'تعداد کاراکتر ها نمی تواند بیش از 150 کاراکتر باشد')
        ]
    )
