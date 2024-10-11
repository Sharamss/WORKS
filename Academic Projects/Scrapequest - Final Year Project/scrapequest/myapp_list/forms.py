from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

##login/signup
class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

##keywords
from django import forms

class KeywordsForm(forms.Form):
    keywords = forms.CharField(widget=forms.Textarea, help_text='Enter keywords separated by commas')

    def __init__(self, *args, **kwargs):
        keywords = kwargs.pop('keywords', [])
        super().__init__(*args, **kwargs)
        self.fields['keywords'].initial = ', '.join(keywords)
