import os
import uuid
from django.db import models
from PIL import Image
import cv2
import numpy as np


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
        return img.size

    def detectar_persona(self):
        """
        Detecta si hay una persona en la imagen.
        """
        face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        )

        img = cv2.imread(self.image.path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(
            gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
        )

        if len(faces) > 0:
            return "Es una persona"
        return "No es una persona"

    def obtener_dpi(self):
        """
        Calcular el dpi de la imagen.
        """
        img = Image.open(self.image.path)
        dpi = img.info.get("dpi")
        return dpi

    def fondo_es_blanco(self):
        """
        Determina si el fondo de la imagen es blanco.
        """
        image = cv2.imread(self.image.path)
        hog = cv2.HOGDescriptor()
        hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
        (rects, weights) = hog.detectMultiScale(image, winStride=(4, 4), padding=(8, 8), scale=1.05)

        if len(rects) > 0:
            message = "Persona detectada!"
        else:
            message = "Persona no detectada"

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        mean = np.mean(gray)

        if mean > 140:
            message = message + " y el fondo es blanco"
        else:
            message = message + " y el fondo no es blanco"

        return message
