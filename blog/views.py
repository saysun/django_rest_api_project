from django.shortcuts import render
from .models import Post

# Create your views here.


def home(request):
    #Post.objects.create(title='blog9', content='First Post Content', author_id=1)
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'blog/about.html',context)
