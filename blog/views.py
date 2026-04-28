from django.shortcuts import render

from .models import Post


def home(request):

    posts = Post.objects.all()

    return render(
        request,
        'home.html',
        {
            'posts': posts
        }
    )

def post_detail(request, slug):

    post = Post.objects.get(slug=slug)

    return render(
        request,
        'post_detail.html',
        {
            'post': post
        }
    )


def sobre(request):
    return render(request, 'sobre.html')