from django import forms
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User


class RegisterUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:  # noqa
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password'
        ]

    def clean(self): # noqa
        cleaned_data = super(RegisterUserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )


class EditUserForm(forms.ModelForm): # noqa
    current_password = forms.CharField(widget=forms.PasswordInput, help_text='Required to make any changes')

    class Meta:  # noqa
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
        ]

    def clean(self): # noqa
        cleaned_data = super(EditUserForm, self).clean()
        current_password = cleaned_data['current_password']

        if not check_password(current_password, self.instance.password):
            raise forms.ValidationError(
                'Current password was not valid'
            )
