from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Institucion(models.Model):
    nombre = models.CharField(max_length=100)

class Credito(models.Model):
    nombre = models.CharField(max_length=100)
    interes = models.FloatField()
    plazo_meses = models.IntegerField()
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE, related_name='creditos')

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE, related_name='administradores')
