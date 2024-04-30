# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InstitucionViewSet, CreditoViewSet, AdminViewSet, InversionViewSet, LoginView

router = DefaultRouter()
router.register(r'instituciones', InstitucionViewSet, basename="institucion")
router.register(r'creditos', CreditoViewSet, basename="credito")
router.register(r'inversiones', InversionViewSet, basename="inversion")
router.register(r'admins', AdminViewSet, basename="admin")

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginView.as_view()),
]
