from django import forms
from .models import Comment,Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm


class CommentModel(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["user_name", "user_email", "text"]
        labels = {
            "user_name": "Your Name",
            "user_email": "Your Email",
            "text": "Your Comment"
        }

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ["user", "slug", "date",]

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields=("username", "email", "password1", "password2")        


# class LoginForm(AuthenticationForm):
#     class Meta:
#         fields = ("username", "password")
    