from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib import messages


def login_view(request):
    """
    Login del sistema.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        usuario = authenticate(username=username, password=password)
        if usuario:
            login(request, usuario)
            messages.success(request, f'Bienvenido {usuario.username}')
            return redirect('index')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')

    return render(request, 'usuarios/login.html', {})


def logout_view(request):
    """
    Salir del sistema.
    """
    logout(request)
    messages.success(request, 'Sesion cerrada con exito.')
    return redirect('login')


def index(request):
    """
    Pagina de inicio del sistema.
    """
    return render(request, 'index.html', {})
