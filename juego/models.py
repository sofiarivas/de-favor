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
    PLATFORM_CHOICES = sorted({
        ('xbox', 'Xbox'),
        ('xbox360', 'Xbox 360'),
        ('xboxone', 'Xbox One'),
        ('ps2', 'Playstation 2'),
        ('ps3', 'Playstation 3'),
        ('ps4', 'Playstation 4'),
        ('wii', 'Nintendo Wii')
    })
    STATE_CHOICES = sorted({
        ('AGU', 'Aguascalientes'), ('BCN', 'Baja California'),
        ('BCS', 'Baja California Sur'),
        ('CAM', 'Campeche'), ('CHH', 'Chihuahua'),
        ('CHP', 'Chiapas'), ('COA', 'Coahuila'),
        ('COL', 'Colima'),
        ('CDMX', 'Ciudad de Mexico'),
        ('DUR', 'Durango'), ('GRO', 'Guerrero'),
        ('GUA', 'Guanajuato'), ('HID', 'Hidalgo'),
        ('JAL', 'Jalisco'), ('MEX', 'Estado de México'),
        ('MIC', 'Michoacán'), ('MOR', 'Morelos'),
        ('NAY', 'Nayarit'), ('NLE', 'Nuevo León'),
        ('OAX', 'Oaxaca'), ('PUE', 'Puebla'),
        ('QUE', 'Querétaro'), ('ROO', 'Quintana Roo'),
        ('SIN', 'Sinaloa'), ('SLP', 'San Luis Potosí'),
        ('SON', 'Sonora'), ('TAB', 'Tabasco'),
        ('TAM', 'Tamaulipas'), ('TLA', 'Tlaxcala'),
        ('VER', 'Veracruz'), ('YUC', 'Yucatán'),
        ('ZAC', 'Zacatecas')})

    usuario = models.ForeignKey(User, related_name='propietario',
                                blank=True, null=True)
    titulo = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    plataforma = models.CharField(max_length=50, db_index=True,
                                  choices=PLATFORM_CHOICES)
    categoria = models.ForeignKey(Categoria, related_name='categoria')
    fecha_alta = models.DateTimeField(auto_now=True)
    precio_renta = models.FloatField(blank=True, null=True)
    deposito = models.FloatField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    ubicacion = models.CharField(max_length=100, choices=STATE_CHOICES)
    imagen = models.ImageField(upload_to='media')
    prefijo = models.CharField(max_length=3)
    telefono = models.CharField(max_length=10)
