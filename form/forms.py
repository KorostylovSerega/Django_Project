from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class EnglishLevelForm(forms.Form):
    MALE = 'M'
    FEMALE = 'F'
    GENDER = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    ELEMENTARY = 'A1'
    PRE_INTERMEDIATE = 'A2'
    INTERMEDIATE = 'B1'
    UPPER_INTERMEDIATE = 'B2'
    ADVANCED = 'C1'
    PROFICIENCY = 'C2'
    ENGLISH_LANGUAGE_LEVEL = [
        (ELEMENTARY, 'Elementary (A1)'),
        (PRE_INTERMEDIATE, 'Pre-Intermediate (A2)'),
        (INTERMEDIATE, 'Intermediate (B1)'),
        (UPPER_INTERMEDIATE, 'Upper-Intermediate (B2)'),
        (ADVANCED, 'Advanced (C1)'),
        (PROFICIENCY, 'Proficiency (C2)'),
    ]
    name = forms.CharField(label='Name', max_length=50)
    age = forms.IntegerField(label='Age')
    gender = forms.ChoiceField(label='Gender', choices=GENDER)
    english_level = forms.ChoiceField(label='English language level', choices=ENGLISH_LANGUAGE_LEVEL)

    def clean(self):
        cleaned_data = super().clean()
        gender = cleaned_data.get('gender')
        age = cleaned_data.get('age')
        english_level = cleaned_data.get('english_level')
        if gender == 'M':
            if age < 20:
                self.add_error('age', 'Age must be over 20 years old')
            if english_level == self.ELEMENTARY or \
                    english_level == self.PRE_INTERMEDIATE or \
                    english_level == self.INTERMEDIATE:
                self.add_error('age', 'English proficiency must be at B2 level or higher')
        elif gender == 'F':
            if age < 22:
                self.add_error('age', 'Age must be over 22 years old')
            if english_level == self.ELEMENTARY or english_level == self.PRE_INTERMEDIATE:
                self.add_error('age', 'English proficiency must be at B1 level or higher')


class AuthenticationForm(forms.Form):
    username = forms.CharField(max_length=100, label='Login')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        if username and password:
            self.user = authenticate(username=username, password=password)
            if self.user is None:
                raise forms.ValidationError('Incorrect username or password')


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=100, label='Login')
    email = forms.EmailField(max_length=100, label='Email')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Repeat password')

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        if User.objects.filter(username=username).exists():
            self.add_error('username', 'User with the same name already exists')
        if User.objects.filter(email=email).exists():
            self.add_error('email', 'This email is already registered')
        if password != password2:
            self.add_error('password2', 'Password entered incorrectly')


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput, label='Old password')
    new_password = forms.CharField(widget=forms.PasswordInput, label='New password')
    new_password2 = forms.CharField(widget=forms.PasswordInput, label='New password repeat')

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        old_password = cleaned_data.get('old_password')
        new_password = cleaned_data.get('new_password')
        new_password2 = cleaned_data.get('new_password2')
        if not self.user.check_password(old_password):
            self.add_error('old_password', 'Invalid password')
        if old_password == new_password:
            self.add_error('new_password', 'Passwords must be different')
        if new_password != new_password2:
            self.add_error('new_password2', 'Password entered incorrectly')


class CommentsFinderForm(forms.Form):
    comment = forms.CharField(max_length=200, label='Enter a request')
    author = forms.BooleanField(required=False, label='Search only your comments')
