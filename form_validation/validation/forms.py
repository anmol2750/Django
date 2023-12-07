from django.forms import ModelForm
from django import forms
from validation.models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'gender', 'password']

    def clean(self):
        super(UserForm, self).clean()

        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if len(username) < 5:
            self._errors['username'] = self.error_class(['A Minimum of 8 characters required'])

        if User.objects.filter(username = username).exists():
            self.errors['username'] = self.error_class(['Username already exists'])

        if User.objects.filter(email = email).exists():
            self.errors['email'] = self.error_class(['Email already exists'])
    
        if len(password) < 8:
            self._errors['password'] = self.error_class(['Password length should not be less than 8 characters'])

        return self.cleaned_data