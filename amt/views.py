from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Institucion, Admin, Credito, Inversion
from .serializers import InstitucionSerializer, CreditoSerializer, AdminSerializer, InversionSerializer

# Create your views here.
class InstitucionViewSet(viewsets.ModelViewSet):
    queryset = Institucion.objects.all()
    serializer_class = InstitucionSerializer

class CreditoViewSet(viewsets.ModelViewSet):
    queryset = Credito.objects.all()
    serializer_class = CreditoSerializer

class InversionViewSet(viewsets.ModelViewSet):
    queryset = Inversion.objects.all()
    serializer_class = InversionSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Extract institution_id from the request data
        institution_id = request.data.get('institucion_id')

        # Check if the institution with the given ID exists
        try:
            institucion = Institucion.objects.get(pk=institution_id)
        except Institucion.DoesNotExist:
            return Response({"error": "Institucion does not exist."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Create a new admin with the specified institution
        admin = serializer.save(institucion=institucion)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Extract institution_id from the request data
        institution_id = request.data.get('institucion_id')

        # Check if the institution with the given ID exists
        try:
            institucion = Institucion.objects.get(pk=institution_id)
        except Institucion.DoesNotExist:
            return Response({"error": "Institucion does not exist."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Create a new admin with the specified institution
        admin = serializer.save(institucion=institucion)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class LoginView(APIView):

    def post(self, request, format=None):
        users = Admin.objects.all()
        for u in users:
            if u.username == request.data['username'] and u.password == request.data["password"]:
                return Response(data={
                    "institucion": u.institucion.id if u.institucion else None,
                    "admin": u.is_superuser,
                }, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
