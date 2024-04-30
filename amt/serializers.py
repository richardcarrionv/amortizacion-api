# serializers.py
from rest_framework import serializers
from .models import Institucion, Credito, Admin, Inversion


class CreditoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Credito
        fields = '__all__'

class InversionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Inversion
        fields = ("id", "tipo", "tiempo", "interes")

class InstitucionSerializer(serializers.ModelSerializer):
    creditos = CreditoSerializer(many=True, read_only=True)
    inversiones = InversionSerializer(many=True, read_only=True)

    class Meta:
        model = Institucion
        fields = '__all__'

class AdminSerializer(serializers.ModelSerializer):
    institucion = InstitucionSerializer(read_only=True)
    class Meta:
        model = Admin
        fields = ("password", "is_superuser", "username", "institucion")
