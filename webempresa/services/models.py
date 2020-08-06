from django.db import models

# Create your models here.
class service(models.Model):
    Title=models.CharField(verbose_name='Título',max_length=200)
    Subtitle=models.CharField(verbose_name='Subtítulo',max_length=200)
    Content=models.TextField(verbose_name='Contenido')
    Image=models.ImageField(verbose_name='Imagen',upload_to='services')
    Created=models.DateTimeField(verbose_name='Fecha de creación',auto_now_add=True)
    Updated=models.DateTimeField(verbose_name='Fecha de edición',auto_now=True)

    class Meta:
        verbose_name='Servicio'
        verbose_name_plural='Servicios'
        ordering=['Created']

    def __str__(self):
	    return self.Title