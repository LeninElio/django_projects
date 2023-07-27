import uuid
from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save

# Create your models here.
class Product(models.Model):
    """
    Modelo productos.
    """
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=8, default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=False, null=True, unique=True)
    image = models.ImageField(upload_to='productos/', null=False, blank=False)


    def __str__(self):
        return ''+self.title


    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super(Product, self).save(*args, **kwargs)


def set_slug(sender, instance, *args, **kwargs):
    if instance.title and not instance.slug:
        slug = slugify(instance.title)

        while Product.objects.filter(slug=slug).exists():
            slug = slugify(
                f'{instance.title}-{str(uuid.uuid4())[:8]}'
            )

        instance.slug = slug

pre_save.connect(set_slug, sender=Product)
