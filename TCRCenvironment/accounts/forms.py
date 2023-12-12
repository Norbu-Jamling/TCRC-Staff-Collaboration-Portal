from django import forms
from django.contrib.auth.models import User
from accounts.models import UserProfile
from django.contrib.auth.forms import UserChangeForm, AuthenticationForm, UsernameField
from django.forms import ModelForm

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(
        attrs={
            'type':'text',
            'class': 'input-field',
            'placeholder': 'User ID',
              }
              ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'type': 'password',
            'class': 'input-field',
            'placeholder': 'Password',
        }
))
    
class EditProfileForm(ModelForm):
    class Meta:
        model=UserProfile
        fields=('name','department','role','current_project',)
    
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'type':'text',
            'class': 'input-field',
            'placeholder': 'Name',
              }
              ))
    department = forms.CharField(widget=forms.TextInput(
        attrs={
            'type':'text',
            'class': 'input-field',
            'placeholder': 'Department',
              }
              ))
    role = forms.CharField(widget=forms.TextInput(
        attrs={
            'type':'text',
            'class': 'input-field',
            'placeholder': 'Role',
              }
              ))
    current_project = forms.CharField(widget=forms.TextInput(
        attrs={
            'type':'text',
            'class': 'input-field',
            'placeholder': 'Current Project',
              }
              ))
        
        
