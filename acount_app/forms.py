# forms.py
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from .models import User, Address


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField( widget=forms.PasswordInput(attrs={'class': 'input-field', 'placeholder': 'نام کاربری'}))
    password2 = forms.CharField( widget=forms.PasswordInput(attrs={'class': 'input-field', 'placeholder': 'رمز عبور'}))

    class Meta:
        model = User
        fields = ["username"]

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ["username", "password", "is_active", "is_admin"]


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder':'ایمیل یا شماره تماس رو وارد کنید'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input-field', 'placeholder': 'رمز عبور'})
    )


class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(
        label="رمز عبور",
        widget=forms.PasswordInput(attrs={'class': 'input-field', 'placeholder': 'رمز عبور'})
    )
    password2 = forms.CharField(
        label="تکرار رمز عبور",
        widget=forms.PasswordInput(attrs={'class': 'input-field', 'placeholder': 'تکرار رمز عبور'})
    )

    class Meta:
        model = User
        fields = ("username",)

        widgets = {
            "username": forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'ایمیل یا شماره تماس رو وارد کنید'}),
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd.get("password1") != cd.get("password2"):
            raise ValidationError("رمزها یکسان نیستند")
        return cd.get("password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class AddressForm(forms.ModelForm):
    user = forms.IntegerField(required=False)
    class Meta:
        model = Address
        fields = '__all__'