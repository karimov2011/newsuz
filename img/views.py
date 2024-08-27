from django.shortcuts import render
from .models import *


def home(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'home.html', context)

def details(request, id):
    post = Post.objects.get(id=id)
    context = {'post':post}
    return render(request, 'post_details.html', context)


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')