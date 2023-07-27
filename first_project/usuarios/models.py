from datetime import datetime
from django.db import models

# Create your models here.
class Usuario(models.Model):
    """
    Modelo que representa a un usuario
    """
    nombre = models.CharField('Nombre de la persona', max_length=30)
    apellido_paterno = models.CharField('Apellido paterno de la persona', max_length=30)
    apellido_materno = models.CharField('Apellido materno de la persona', max_length=30)
    producto = models.ManyToManyField('Producto', verbose_name='Productos del usuario')


STATUS_CHOICES = (
    ('L', 'Leido'),
    ('N', 'No leido'),
    ('E', 'Error'),
    ('A', 'Aceptado')
)


class Web(models.Model):
    """
    Modelo que representa a una web
    """
    nombre = models.CharField(max_length=50)
    url = models.URLField()
    data = models.DateField()
    valoracion = models.IntegerField()
    # cuando el usuario se elimine, se eliminan todas sus webs
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    estado = models.CharField(choices=STATUS_CHOICES, max_length=1)


    def tiempo_post(self):
        """
        Método que devuelve el tiempo que lleva publicado el post
        """
        if self.data < datetime.now().date(2022, 1, 1):
            return 'Publicado hace mucho tiempo'
        return 'Publicado hace poco tiempo'


class Producto(models.Model):
    """
    Modelo que representa a un producto
    """
    nombre = models.CharField(max_length=50, primary_key=True)
    precio = models.IntegerField(max_length=20)
    estado = models.BooleanField(default=False)
    anio = models.IntegerField(max_length=10)


    # class Meta:
    #     """
    #     Clase que contiene los metadatos del modelo
    #     """
    #     orden = ['precio']
    #     verbose_name = 'El producto'
    #     verbose_name_plural = 'Los productos'


    def nombre_completo(self):
        """
        Método que devuelve el nombre completo del producto
        """
        return f'El nombre completo es: {self.nombre}'


    def __str__(self):
        return '' + self.nombre
