from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('grados/<grado>', views.info_grados, name="grados"),
    path('grados/<grado>/<universidad>', views.info_grados_universidad, name="grados_universidad"),
    path('animo', views.animo, name="animo"),
    path('animo/<blog>', views.animo_blogs, name="animo_blogs"),
    path('contacto', views.contacto, name="contacto"),
    path('comentario', views.gestion_comentario, name="comentario")
]