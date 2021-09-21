from django import forms
from django.forms.formsets import MAX_NUM_FORM_COUNT
from .models import Post
from blog import models


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content')


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email_address = forms.EmailField(max_length=50)
    message = forms.CharField(widget=forms.Textarea, max_length=2000)
