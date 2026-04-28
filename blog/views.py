from django.shortcuts import render, get_object_or_404

from django.core.paginator import Paginator

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


def sobre(request):

    return render(
        request,
        'sobre.html'
    )


def posts(request):

    busca = request.GET.get('busca')

    categoria = request.GET.get('categoria')

    ordenacao = request.GET.get(
        'ordenacao'
    )

    if ordenacao == 'antigos':

        posts = Post.objects.order_by(
            'data_criacao'
        )

    elif ordenacao == 'az':

        posts = Post.objects.order_by(
            'titulo'
        )

    else:

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

    paginator = Paginator(
        posts,
        3
    )

    page = request.GET.get('page')

    posts = paginator.get_page(page)

    return render(
        request,
        'posts.html',
        {
            'posts': posts
        }
    )


def post_detail(request, slug):

    post = get_object_or_404(
        Post,
        slug=slug
    )

    return render(
        request,
        'post_detail.html',
        {
            'post': post
        }
    )