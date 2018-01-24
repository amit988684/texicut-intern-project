
from django import forms

class NameForm(forms.Form):
    chat = forms.CharField(widget=forms.PasswordInput)