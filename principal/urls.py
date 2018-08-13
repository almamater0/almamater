from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('grados/<grado>', views.grados, name="grados")
]