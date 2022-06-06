from django.db import models

class Actividad(models.Model):
    actividad = models.CharField('Actividad', max_length = 100) 

    class Meta:
        verbose_name_plural = "Actividades"

    def __str__(self):
        return self.actividad
