from django.db import models
from club.settings import MEDIA_URL
from localidades.models import Localidad
from django.utils.html import mark_safe
from django.conf import settings

class Socio(models.Model):
    apellido = models.CharField('Apellido', max_length=50)
    nombre = models.CharField('Nombre', max_length=50)
    dni = models.CharField('DNI', max_length=10)
    fechanacimiento = models.DateField('Fecha de Nacimiento')
    domicilio = models.CharField('Domicilio', max_length=50)
    telefono = models.CharField('Telefono', max_length=20)
    localidad = models.ForeignKey(Localidad, on_delete=models.RESTRICT, related_name="socio_localidad")
    contactoa = models.CharField('Nombre Contacto 1', max_length=50)
    referentea = models.CharField('Telefono Contacto', max_length=50)
    contactob = models.CharField('Nombre Contacto 2', max_length=50, null=True, blank=True)
    referenteb = models.CharField('Telefono Contacto', max_length=50, null=True, blank=True)
    email = models.EmailField('E-Mail', null=True, blank=True)
    certificadomedico = models.ImageField('Certificado Medico', upload_to ="certificados/", null=True, blank=True)
    bucodental = models.ImageField('Certificado Bucodental', upload_to ="bucodentales/", null=True, blank=True)
    foto = models.ImageField('Foto Carnet', upload_to ="fotos/", null=True, blank=True)

    def __str__(self):
        return self.apellido + ', ' + self.nombre

    def __unicode__(self):
        return self.apellido

    def nombrecompleto(self):
        return self.apellido + ', ' + self.nombre
