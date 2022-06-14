from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class newUserForm(UserCreationForm):
    email=forms.EmailField(label='Email', max_length=50)

    class Meta: 
        model=User
        fields=["username", "email", "password1", "password2"]

    def save(self, commit=True):
        user=super(newUserForm, self).save(commit=True)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class loginForm(UserCreationForm):

    class Meta:
        model=User
        fields=["username","password"]

class PostForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('photo', 'name', 'description')


class ReviewForm(forms.ModelForm):
    text=forms.CharField(widget=forms.Textarea(attrs={'class': 'materialize-textarea'}), required=False)
    usabilityrate=forms.ChoiceField(choices=RATE_CHOICES, widget=forms.Select(),required=True)
    contentrate=forms.ChoiceField(choices=RATE_CHOICES, widget=forms.Select(),required=True)
    designrate=forms.ChoiceField(choices=RATE_CHOICES, widget=forms.Select(),required=True)


    class Meta:
        model=Rate
        fields=( 'usabilityrate', 'contentrate', 'designrate', 'text')


class UpdateUserForm(forms.ModelForm):
    email=forms.EmailField(max_length=254,help_text='Required.Inform a valid email addres')
    class Meta:
        model= User
        fields=('username','email')

class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model= Profile
        fields=('name','bio','profile_pic','location')
