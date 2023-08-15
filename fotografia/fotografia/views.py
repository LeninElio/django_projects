import uuid
from django.shortcuts import render
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
            ancho, alto = imagen_obj.tamano_imagen()

            datos_imagen = {
                'image_size': imagen.size,
                'image_type': imagen.content_type,
                'imagen_url': image_url,
                'ancho': ancho,
                'alto': alto,
                'persona': imagen_obj.detectar_persona(),
                "dpi": imagen_obj.obtener_dpi(),
                'fondo': imagen_obj.fondo_es_blanco(),
            }

            return render(request, 'upload.html', datos_imagen)

    return render(request, '404.html')
    # return HttpResponse('Error al subir la imagen.')
