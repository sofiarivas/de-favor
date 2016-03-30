from django.db import models


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
    }
    idproducto = models.IntegerField(primary_key=True)
    slug = models.SlugField(max_length=200, db_index=True)
    titulo = models.CharField(max_length=50, db_index=True)
    plataforma = models.CharField(max_length=50, db_index=True,
                                  choices=PLATFORM_CHOICES)
    categoria = models.ForeignKey(categoria)
    ¡¡!!preciorenta = models.DecimalField(max_digits=None, decimal_places=None)
    ¡¡!!deposito = models.DecimalField(max_digits=None, decimal_places=None)
    descripcion = models.TextField()
    usuario = models.ManyToManyField(User, related_name='juegos')
