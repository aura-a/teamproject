from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Book, Location


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ['title', 'author', 'summary', 'quotes', 'isbn']


class LocationForm(forms.ModelForm):

    class Meta:
        model = Location
        fields = ['name', 'country', 'description']


class ImageUploadForm(forms.Form):
    image = forms.ImageField()


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username',
                  'email',
                  'first_name',
                  'last_name',
                  'password1',
                  'password2',
                  )

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()

        return user


class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
        )

