from django import forms 
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text','photo']

#user reg form inbuit form
class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields =('username','email','password1','password2')
        
class Search(forms.Form):
    query = forms.CharField(max_length=100, label="Search Tweets")
