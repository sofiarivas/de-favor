from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True, unique=True)

    class Meta:
        ordering = ('nombre',)
        verbose_name = 'categoria',
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.nombre


class Juego(models.Model):
    PLATFORM_CHOICES = {
        ('xbox', 'Xbox'),
        ('xbox360', 'Xbox 360'),
        ('xboxone', 'Xbox One'),
        ('ps2', 'Playstation 2'),
        ('ps3', 'Playstation 3'),
        ('ps4', 'Playstation 4'),
        ('wii', 'Nintendo Wii')
    }
    idproducto = models.IntegerField(primary_key=True)
    slug = models.SlugField(max_length=200, db_index=True)
    titulo = models.CharField(max_length=50, db_index=True)
    plataforma = models.CharField(max_length=50, db_index=True,
                                  choices=PLATFORM_CHOICES)
    categoria = models.ForeignKey(Categoria, related_name='juegos')
    preciorenta = models.FloatField(blank=True, null=True)
    deposito = models.FloatField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    usuario = models.ForeignKey(User, related_name='propietario',
                                blank=True, null=True)
    ubicacion = models.ForeignKey(User, related_name='ubicacion')
    imagen = models.ImageField(upload_to='media')
