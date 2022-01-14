from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("imovel/<str:id>", views.imovel, name="imovel"),
    path("agendar_visitas", views.agendar_visitas, name="agendar_visitas"),
]