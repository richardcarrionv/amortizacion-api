from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

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

class LoginView(APIView):

    def post(self, request, format=None):
        users = Admin.objects.all()
        for u in users:
            if u.username == request.data['username'] and u.password == request.data["password"]:
                return Response(data={
                    "institucion": u.institucion.id
                }, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
