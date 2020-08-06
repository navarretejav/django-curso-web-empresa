from django.db import models

# Create your models here.
class Link(models.Model):
    key=models.SlugField(verbose_name='Nombre clave',max_length=100,unique=True)
    name=models.CharField(verbose_name='Red social',max_length=200)
    url=models.URLField(verbose_name='Enlace',max_length=200,blank=True,null=True)
    Created=models.DateTimeField(verbose_name='Fecha de creación',auto_now_add=True)
    Updated=models.DateTimeField(verbose_name='Fecha de edición',auto_now=True)

    class Meta:
        verbose_name='Enlace'
        verbose_name_plural='Enlaces'
        ordering=['name']

    def __str__(self):
	    return self.name
    