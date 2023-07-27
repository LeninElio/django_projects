"""
URL configuration for first_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf  import settings

# Importamos las vistas de nuestro proyecto, views.index es la funcion index.
from productos.views import ProductView
from django.urls import include
from django.conf.urls.static import static
from first_project import views
from first_project.views import MiClase


urlpatterns = [
    path('bienvenido/', views.bienvenido, name='bienvenido'),
    path('clases/', MiClase.as_view(), name='usuarios'),
    path('usuarios/registro', views.registro, name='registro'),
    path('usuarios/logout', views.logout_view, name='logout'),
    path('usuarios/login', views.login_view, name='login'),
    # path('', views.index, name='index'),
    path('', ProductView.as_view(), name='index'),
    path('productos/', include('productos.urls')),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
