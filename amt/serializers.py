# serializers.py
from rest_framework import serializers
from .models import Institucion, Credito, Admin


class CreditoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Credito
        fields = '__all__'

class InstitucionSerializer(serializers.ModelSerializer):
    creditos = CreditoSerializer(many=True, read_only=True)

    class Meta:
        model = Institucion
        fields = '__all__'

class AdminSerializer(serializers.ModelSerializer):
    institucion = InstitucionSerializer(read_only=True)
    class Meta:
        model = Admin
        fields = '__all__'
