from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import rc


class rcf(forms.ModelForm):
    class Meta:
        model = rc
        fields = ('sem', 'course', 'typee', 'title','pdf','dis')

class SignUpForm(UserCreationForm):
    name=forms.CharField(max_length=100, required=False)
    csem= forms.CharField(max_length=100, required=False)
   
    class Meta:
        model = User
        fields = ['username', 'name','csem','password1', 'password2']
      
       