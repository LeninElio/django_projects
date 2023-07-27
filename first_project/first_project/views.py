"""
Dentro de views iran todas las vistas que nosotros vayamos creando
o que necesitemos para nuestro proyecto.
"""
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib import messages
from first_project.forms import Registro
from django.views import View
from productos.models import Product


#para crear una vista, se crea una funcion
# def index(request):
#     """
#     Funcion que devuelve un mensaje.
#     Esto lo debemos registrar esta vista en nuestras urls.
#     """
#     return HttpResponse("Hola mundo!")


# def index(request):
#     """
#     Renderizando un archivo html.
#     """
#     # return render(request, 'index.html', {
#     #     # El tercer parametro es un contexto, es decir, un diccionario.
#     #     # gracias al contexto es que nosotros podemos pasar valores a nuestro template.
#     #     'name': 'Lenin',
#     #     'titulo': 'Index'
#     # })
#     return render(request, 'index.html', {
#         'titulo': 'Personas',
#         'personas': [
#             {'nombre': 'Lenin', 'edad': 22, 'sexo': 'Masculino'},
#             {'nombre': 'Juan', 'edad': 23, 'sexo': 'Masculino'},
#             {'nombre': 'Pedro', 'edad': 24, 'sexo': 'Masculino'},
#             {'nombre': 'Maria', 'edad': 17, 'sexo': 'Femenino'},
#         ]
#     })

def index(request):
    """
    Renderizando un contexto.
    """
    producto = Product.objects.all()
    return render(request, 'index.html', {
        'titulo': 'Productos',
        'productos': producto
    })


def login_view(request):
    """
    Login del sistema.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

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


def registro(request):
    """
    Registro de usuarios.
    """
    form = Registro(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        # username = form.cleaned_data.get('username')
        # email = form.cleaned_data.get('email')
        # password = form.cleaned_data.get('password')

        # usuario = User.objects.create_user(username, email, password)
        usuario = form.save()
        if usuario:
            login(request, usuario)
            messages.success(request, f'Usuario {usuario.username} creado con exito.')
            return redirect('index')

    return render(request, 'usuarios/registro.html', {
        'form': form,
    })


# vista basada en funciones
def bienvenido(request): # pylint: disable=unused-argument
    """
    Vista en funcion de una clase.
    """
    return HttpResponse('Bienvenido al curso')


# vista basada en clases
class MiClase(View):
    """
    Vista basada en clases.
    """
    def get(self, request): # pylint: disable=unused-argument
        """
        Metodo get.
        """
        return HttpResponse('Hola desde la clase')

    def post(self, request): # pylint: disable=unused-argument
        """
        Metodo post.
        """
        return HttpResponse('Hola desde la clase post')
