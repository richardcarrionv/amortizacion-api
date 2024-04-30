from django.db import models
from django.contrib.auth.models import Group, Permission, User, AbstractUser

# Create your models here.

class Institucion(models.Model):
    nombre = models.CharField(max_length=100)
    img = models.TextField(null=True)

class Credito(models.Model):
    nombre = models.CharField(max_length=100)
    interes = models.FloatField()
    plazo_meses = models.IntegerField()
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE, related_name='creditos')

class Inversion(models.Model):
    tipo = models.CharField(max_length=100)
    tiempo = models.IntegerField()
    interes = models.FloatField()
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE, related_name='inversiones')

class Admin(AbstractUser):
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE, related_name='administradores', null=True)

    groups = models.ManyToManyField(Group, related_name='admin_users')
    user_permissions = models.ManyToManyField(Permission, related_name='admin_users')
    
    class Meta:
        verbose_name = 'Administrador'
        verbose_name_plural = 'Administradores'
