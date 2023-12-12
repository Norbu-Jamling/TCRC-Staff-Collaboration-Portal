from django import forms
from home.models import Post

class HomeForm(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={'type':'text',
            'class': 'input-field2',
            'placeholder': 'Enter Message',}
    ))

    class Meta:
        model=Post
        fields=('post',)

