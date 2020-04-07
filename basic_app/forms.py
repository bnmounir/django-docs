from django import forms
from django.core import validators
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')


class FormName(forms.Form):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    verify_email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    text = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control'}))
    b_cat = forms.CharField(required=False,
                            widget=forms.HiddenInput,
                            validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        verify_email = all_clean_data['verify_email']

        if email != verify_email:
            raise forms.ValidationError('email must match!')