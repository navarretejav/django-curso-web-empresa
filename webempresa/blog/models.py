from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name=models.CharField(verbose_name='Nombre',max_length=100)
    created=models.DateTimeField(verbose_name='Fecha de creación',auto_now_add=True)
    updated=models.DateTimeField(verbose_name='Fecha de edición',auto_now=True)

    class Meta:
        verbose_name='Categoría'
        verbose_name_plural='Categorías'
        ordering=['name']

    def __str__(self):
	    return self.name    

class Post(models.Model):
    title=models.CharField(max_length=200,verbose_name='Título')
    content=models.TextField(verbose_name='Contenido')
    published=models.DateTimeField(verbose_name='Fecha de publicación',default=now)
    image=models.ImageField(verbose_name='Imagen',null=True,blank=True,upload_to='blog')
    author=models.ForeignKey(User,verbose_name='Autor',on_delete=models.CASCADE)
    categories=models.ManyToManyField(Category,verbose_name='Categorías',related_name='get_posts')
    created=models.DateTimeField(verbose_name='Fecha de creación',auto_now_add=True)
    updated=models.DateTimeField(verbose_name='Fecha de edición',auto_now=True)

    class Meta:
        verbose_name='Entrada'
        verbose_name_plural='Entradas'
        ordering=['-published']

    def __str__(self):
        return self.title