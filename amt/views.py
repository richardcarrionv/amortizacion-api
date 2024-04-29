from django.shortcuts import render
from rest_framework import viewsets

from .models import Institucion, Admin, Credito
from .serializers import InstitucionSerializer, CreditoSerializer, AdminSerializer

# Create your views here.
class InstitucionViewSet(viewsets.ModelViewSet):
    queryset = Institucion.objects.all()
    serializer_class = InstitucionSerializer

class CreditoViewSet(viewsets.ModelViewSet):
    queryset = Credito.objects.all()
    serializer_class = CreditoSerializer

class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
