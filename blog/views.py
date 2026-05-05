from django.shortcuts import (
    render,
    get_object_or_404,
    redirect
)

from django.core.paginator import Paginator

from .models import (
    Post,
    Comment
)


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

    posts = Post.objects.all()

    if ordenacao == 'antigos':

        posts = posts.order_by(
            'data_criacao'
        )

    elif ordenacao == 'az':

        posts = posts.order_by(
            'titulo'
        )

    else:

        posts = posts.order_by(
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
        9
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

    if request.method == 'POST':

        texto = request.POST.get(
            'texto',
            ''
        ).strip()

        if (
            texto and
            request.user.is_authenticated
        ):

            Comment.objects.create(
                post=post,
                usuario=request.user,
                texto=texto
            )

        return redirect(
            'post_detail',
            slug=post.slug
        )

    comments = post.comments.order_by(
        '-data_criacao'
    )

    return render(
        request,
        'post_detail.html',
        {
            'post': post,
            'comments': comments
        }
    )


def like_post(request, slug):

    post = get_object_or_404(
        Post,
        slug=slug
    )

    if request.user.is_authenticated:

        if request.user in post.likes.all():

            post.likes.remove(
                request.user
            )

        else:

            post.likes.add(
                request.user
            )

    return redirect(
        'post_detail',
        slug=post.slug
    )