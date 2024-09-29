from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

# Create your views here.
posts = Post.objects.all()

def index(request):
    return render(
        request,
        'blog/index.html',
        {
            'posts' : posts,
        }
    )

#portfolio-details.html

def portfolio(request):
    return render(
        request,
        'blog/portfolio-details.html',
        {
            'posts' : posts,
        }
    )
