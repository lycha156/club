from django.db import models

class Localidad(models.Model):
    localidad = models.CharField('Localidad', max_length = 100)

    class Meta:
        verbose_name_plural = "Localidades"
        
    def __str__(self):
        return self.localidad
