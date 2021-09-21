from django import forms
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .models import Post
from blog import *

from .forms import PostForm, ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

# Create your views here.


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_lists.html', {'posts': posts})

# POST METHOD


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publish_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form, 'pk': pk})


def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post:
        post.delete()
        posts = Post.objects.all()
    return render(request, 'blog/post_lists.html', {'posts': posts})


# SEND EMAIL

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Title of message"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email_address': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message']
            }
            message = '\n'.join(body.values())
            try:
                send_mail(subject, message, 'from@gmail.com',
                          ['to_help@gmail.com'])

            except BadHeaderError:
                return (HttpResponse('Find incorrect header'))
            return redirect('post_list')
    form = ContactForm()
    return render(request, 'blog/contact.html', {'form': form})
