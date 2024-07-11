from django.shortcuts import render
from .models import Post

posts = [
    {
        'author': 'Coco',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'June 9, 2024'
    },
    {
        'author': 'Koko',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'June 19, 2024'
    }
]

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
