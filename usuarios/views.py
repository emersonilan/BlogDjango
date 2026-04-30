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


def cadastro_view(request):

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

        if User.objects.filter(
            username=username
        ).exists():

            return render(
                request,
                'usuarios/cadastro.html',
                {
                    'erro':
                    'Usuário já existe'
                }
            )

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect('login')

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

            return redirect('/')

        return render(
            request,
            'usuarios/login.html',
            {
                'erro':
                'Usuário ou senha inválidos'
            }
        )

    return render(
        request,
        'usuarios/login.html'
    )


def logout_view(request):

    logout(request)

    return redirect('/')