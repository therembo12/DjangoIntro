from datetime import date
from django.shortcuts import render
from django.utils import timezone

from .models import Post
from blog import *
# Create your views here.


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_lists.html', {'posts': posts})
