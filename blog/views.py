from django.shortcuts import redirect, render, get_object_or_404

from django.core.paginator import Paginator

from .models import Post, Comment


def home(request):

    posts = Post.objects.order_by('-data_criacao')[:3]

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

    ordenacao = request.GET.get('ordenacao')

    posts = Post.objects.all()

    if ordenacao == 'antigos':

        posts = posts.order_by('data_criacao')

    elif ordenacao == 'az':

        posts = posts.order_by('titulo')

    else:

        posts = posts.order_by('-data_criacao')

    if busca:

        posts = posts.filter(
            titulo__icontains=busca
        )

    if categoria:

        posts = posts.filter(
            categoria__nome=categoria
        )

    paginator = Paginator(posts, 3)

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

    post = get_object_or_404(Post, slug=slug)

    if request.method == 'POST':

        nome = request.POST.get('nome', '').strip()
        texto = request.POST.get('texto', '').strip()

        if nome and texto:

            Comment.objects.create(
                post=post,
                nome=nome,
                texto=texto
            )

        # 🔴 ISSO EVITA DUPLICAÇÃO NO F5
        return redirect('post_detail', slug=post.slug)

    comments = post.comments.order_by('-data_criacao')

    return render(
        request,
        'post_detail.html',
        {
            'post': post,
            'comments': comments
        }
    )

from django.shortcuts import redirect

def like_post(request, slug):

    post = get_object_or_404(Post, slug=slug)

    post.likes += 1

    post.save()

    return redirect('post_detail', slug=post.slug)