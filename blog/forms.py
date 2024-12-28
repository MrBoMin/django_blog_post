from django import forms 
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from .models import Post

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']



class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content','image','status']
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'content' : forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class':'form-control'})

        }
