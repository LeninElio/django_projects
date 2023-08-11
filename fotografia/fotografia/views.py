import uuid
from django.shortcuts import render
from django.http import HttpResponse
from procesar.models import Picture


def index(request):
    """
    Inicio del sistema.
    """
    return render(request, 'index.html', {})


def upload(request):
    """
    Subir imagen.
    """
    if request.method == 'POST':
        imagen = request.FILES.get('image')
        if imagen:

            unique_filename = f"{uuid.uuid4()}.{imagen.name.split('.')[-1]}"

            imagen_obj = Picture(image=imagen, nombre_archivo=unique_filename)
            imagen_obj.save()

            image_url = imagen_obj.image.url

            return render(request, 'upload.html',
                          {'image_size': imagen.size,
                           'image_type': imagen.content_type,
                           'imagen_url': image_url,
                           'tamano': imagen_obj.tamano_imagen()}
                           )

    return HttpResponse('Error al subir la imagen.')
