import uuid
from django.db import models
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.db.models.signals import pre_save


class Platform(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name='Plataforma')
    icon = models.ImageField(upload_to='platforms/icons/', null=False, blank=False, default='platforms/icons/default_icon.png', verbose_name='Icono')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Plataforma'
        verbose_name_plural = 'Plataformas'
        ordering = ['name']

class Format(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name='Formato')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Formato'
        verbose_name_plural = 'Formatos'
        ordering = ['name']

class Videogame(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Propietario')
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='Título')
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE, verbose_name='Plataforma')
    formato = models.ForeignKey(Format, on_delete=models.CASCADE, verbose_name='Formato') # format no disponible
    release_date = models.DateField(null=True, blank=True, verbose_name='Fecha de lanzamiento')
    front_cover = models.ImageField(upload_to='videogames/front_covers/', null=False, blank=False, default='videogames/front_covers/default_front_cover.png', verbose_name='Carátula')
    description = models.TextField(blank=True, default='', verbose_name='Descripción')
    slug = models.SlugField(null=False, blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse_lazy("videogame_view", args=[str(self.slug)])

    class Meta:
        verbose_name = 'Videojuego'
        verbose_name_plural = 'Videojuegos'
        ordering = ['title']

def set_slug(sender, instance, *args, **kwargs):
    if instance.title and not instance.slug:
        slug = slugify(f"{str(uuid.uuid4())}")
    
        while Videogame.objects.filter(slug=slug).exists():
            slug = slugify(f"{str(uuid.uuid4())}")
    
        instance.slug = slug

pre_save.connect(set_slug, sender=Videogame)