from django import forms
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm


class RegistrationForm(forms.ModelForm):

    password = forms.CharField(widget = forms.PasswordInput)
    password_confirmation = forms.CharField(widget = forms.PasswordInput)


    class Meta:
        model = CustomUser
        fields = [
            'username',
            'email',
            'password',
            'password_confirmation',
        ]



    # Checking for validation
    # and password matching

    def clean(self):

        # First perform normal validation
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        password_confirmation = cleaned_data.get('password_confirmation')

        if password and password_confirmation :
            if password != password_confirmation :
                raise forms.ValidationError(
                    'Passwords do not match.'
                )

        return cleaned_data 


    # After validation
    # saving the password


    def save(self, commit = True):
        user = super().save(commit = False)

        user.set_password(
            self.cleaned_data['password']
        )

        if commit:
            user.save()

        return user


# Creating a Login form

class LoginForm(AuthenticationForm):
    pass
