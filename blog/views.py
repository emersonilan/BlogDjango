from django.shortcuts import render

from .models import Post


def home(request):

    posts = Post.objects.order_by(
    '-data_criacao'
)[:3]

    return render(
        request,
        'home.html',
        {
            'posts': posts
        }
    )

def posts(request):

    busca = request.GET.get('busca')

    categoria = request.GET.get('categoria')

    posts = Post.objects.order_by(
        '-data_criacao'
    )

    if busca:

        posts = posts.filter(
            titulo__icontains=busca
        )

    if categoria:

        posts = posts.filter(
            categoria__nome=categoria
        )

    return render(
        request,
        'posts.html',
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