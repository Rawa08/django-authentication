from django import forms


class UserLoginForm(forms.Form):
    """Form to login for users"""

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)