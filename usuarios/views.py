from .forms import (
    PerfilForm,
    UserForm
)

from django.shortcuts import (
    render,
    redirect
)

from django.contrib.auth.models import User

from django.contrib.auth import (
    authenticate,
    login,
    logout
)

from .models import Perfil

from .forms import PerfilForm


def cadastro(request):

    if request.method == 'POST':

        username = request.POST.get(
            'username'
        )

        email = request.POST.get(
            'email'
        )

        password = request.POST.get(
            'password'
        )

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect(
            'login'
        )

    return render(
        request,
        'usuarios/cadastro.html'
    )


def login_view(request):

    if request.method == 'POST':

        username = request.POST.get(
            'username'
        )

        password = request.POST.get(
            'password'
        )

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:

            login(
                request,
                user
            )

            return redirect(
                'home'
            )

    return render(
        request,
        'usuarios/login.html'
    )


def logout_view(request):

    logout(request)

    return redirect(
        'home'
    )


def perfil(request):

    perfil = request.user.perfil

    comentarios = (
        request.user.comment_set.all()
    )

    posts_curtidos = (
        request.user.liked_posts.all()
    )

    return render(
        request,
        'usuarios/perfil.html',
        {
            'perfil': perfil,
            'comentarios': comentarios,
            'posts_curtidos': posts_curtidos
        }
    )

def perfil_usuario(
    request,
    username
):

    user = User.objects.get(
        username=username
    )

    perfil = user.perfil

    comentarios = (
        user.comment_set.all()
    )

    posts_curtidos = (
        user.liked_posts.all()
    )

    return render(
        request,
        'usuarios/perfil.html',
        {
            'perfil': perfil,
            'comentarios': comentarios,
            'posts_curtidos': posts_curtidos,
            'perfil_user': user
        }
    )

def editar_perfil(request):

    perfil = request.user.perfil

    if request.method == 'POST':

        user_form = UserForm(
            request.POST,
            instance=request.user
        )

        perfil_form = PerfilForm(
            request.POST,
            request.FILES,
            instance=perfil
        )

        if (
            user_form.is_valid()
            and perfil_form.is_valid()
        ):

            user_form.save()

            perfil_form.save()

            return redirect(
                'perfil'
            )

    else:

        user_form = UserForm(
            instance=request.user
        )

        perfil_form = PerfilForm(
            instance=perfil
        )

    return render(
        request,
        'usuarios/editar_perfil.html',
        {
            'user_form': user_form,
            'perfil_form': perfil_form
        }
    )