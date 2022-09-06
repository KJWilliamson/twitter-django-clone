from django import forms
from twitteruser.models import TwitterUser


class SignupForm(forms.ModelForm):
    class Meta:
        model = TwitterUser
        fields = ['username', 'password']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
