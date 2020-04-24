from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from accounts.models import Customer


class UserLoginForm(forms.Form):
    """
    Form to be used to log users input
    """
    username = forms.CharField(label='Username *',
                               widget=forms.TextInput
                               ({'placeholder': 'Enter Username'}),
                               required=True)
    password = forms.CharField(widget=forms.PasswordInput
                               ({'placeholder': 'Enter Password'}),
                               required=True)


class UserRegistrationForm(UserCreationForm):
    """
    Form used to register a new user
    """
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput({'placeholder': 'Enter Password'}),
        required=True)
    password2 = forms.CharField(
        label="Password Confirmation",
        widget=forms.PasswordInput({'placeholder': 'Re-Enter Password'}),
        required=True)

    class Meta:
        """
        Meta class is a sub-class used to house detail within overall
        'UserRegistrationForm' class.
        """
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):  # Clean is preventing dirty data in DB
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'Email address must be unique')
        return email

    def clean_password2(self):  # Clean is preventing dirty data in DB
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password1 or not password2:
            raise ValidationError("Please confirm your password")

        if password1 != password2:
            raise ValidationError("Passwords must match")

        return password2


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            "full_name",
            "phone_number",
            "postcode",
            "town_city",
            "street_address1",
            "street_address2",
            "county",
        ]
