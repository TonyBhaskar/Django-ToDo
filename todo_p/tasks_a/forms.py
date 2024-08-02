from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=35, required=False)

    class Meta:
        model = User
        fields = ['first_name','username', 'password1', 'password2']

    def save(self, commit = True):
        user = super(SignUpForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']

        if commit:
            user.save()
        return user