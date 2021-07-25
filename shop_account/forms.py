from django import forms
from django.contrib.auth.models import User
from django.core import validators

from shop_account.models import UserProfile


class LoginForm(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'username'}),
        validators=[
            validators.MinLengthValidator(1, 'error')
        ]
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'password'}),
        validators=[
            validators.MinLengthValidator(1, 'error')
        ]
    )

    def clean_user_name(self):
        user_name = self.cleaned_data.get('user_name')
        is_exist = User.objects.filter(username=user_name).exists()
        if not is_exist:
            raise forms.ValidationError('username not found')

        return user_name


class RegisterForm(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'username'}),
        validators=[
            validators.MinLengthValidator(1, 'error')
        ]
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'email'}),
        validators=[
            validators.MinLengthValidator(1, 'error')
        ]
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'password'}),
        validators=[
            validators.MinLengthValidator(1, 'error')
        ]
    )

    re_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'password'}),
        validators=[
            validators.MinLengthValidator(1, 'error')
        ]
    )

    def clean_user_name(self):
        user_name = self.cleaned_data.get('user_name')
        is_exist = User.objects.filter(username=user_name).exists()
        if is_exist:
            raise forms.ValidationError('نام کاربری تکراری است')

        return user_name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        is_exist = User.objects.filter(username=email).exists()
        if is_exist:
            raise forms.ValidationError('ایمیل تکراری است')

        return email

    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        if re_password != password:
            raise forms.ValidationError('پسورد برابر نیست')


class EditUserForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'نام', 'class': 'form-control'})
    )

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'نام خانوادگی', 'class': 'form-control'})
    )

    profile_image = forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={'class': 'form-control', 'accept': 'user-profile/'}),
        label='تصویر پروفایل'
    )


class CreateAddressForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'نام', 'class': 'form-control'}),
        validators=[
            validators.MinLengthValidator(1, 'لطفا مقداری وارد کنید'),
            validators.MaxLengthValidator(150, 'کاراکتر ها زیاد است')
        ]
    )

    family = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'نام خانوادگی', 'class': 'form-control'}),
        validators=[
            validators.MinLengthValidator(1, 'لطفا مقداری وارد کنید'),
            validators.MaxLengthValidator(150, 'کاراکتر ها زیاد است')
        ]
    )

    city = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'شهر', 'class': 'form-control'}),
        validators=[
            validators.MinLengthValidator(1, 'لطفا مقداری وارد کنید'),
            validators.MaxLengthValidator(150, 'کاراکتر ها زیاد است')
        ]
    )

    full_address = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'آدرس کامل', 'class': 'form-control', 'rows': '7', 'cols': '20'}),
        validators=[
            validators.MinLengthValidator(1, 'لطفا مقداری وارد کنید')
        ]
    )

    post_code = forms.CharField(
        widget=forms.NumberInput(attrs={'placeholder': 'کدپستی', 'class': 'form-control'}),
        validators=[
            validators.MinLengthValidator(1, 'لطفا مقداری وارد کنید'),
            validators.MaxLengthValidator(150, 'کاراکتر ها زیاد است')
        ]
    )

    phone_number = forms.CharField(
        widget=forms.NumberInput(attrs={'placeholder': 'شماره تلفن', 'class': 'form-control'}),
        validators=[
            validators.MinLengthValidator(1, 'لطفا مقداری وارد کنید'),
            validators.MaxLengthValidator(150, 'کاراکتر ها زیاد است')
        ]
    )
