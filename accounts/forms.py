from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("email","name", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        if commit:
            user.save()
        return user

class modifyAccount():
    class Meta:
        model = User
        fields = ("username","email","password3","password1", "password2")

    def save(self, commit=True):
        user = super(modifyAccount, self).save(commit=False)
        if commit:
            user.save()
        return user

class validation():
    class Meta:
        fields = ("code")
