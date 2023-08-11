import os
import uuid
from django.db import models
from PIL import Image


def generate_filename(instance, filename):
    """
    Genera un nombre de archivo único.
    """
    ext = filename.split('.')[-1]
    unique_filename = f"{uuid.uuid4()}.{ext}"
    return os.path.join('imagenes/', unique_filename)


class Picture(models.Model):
    """
    Modelo Imagen.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=generate_filename, null=False, blank=False)
    nombre_archivo = models.CharField(max_length=255)


    def tamano_imagen(self):
        """
        Retorna el tamaño de la imagen.
        """
        img = Image.open(self.image.path)
        ancho, alto = img.size
        return f"{ancho}x{alto}"
