from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('grados', views.lista_grados, name="lista_grados"),
    path('grados/<grado>', views.info_grados, name="grados"),
    path('grados/<grado>/<universidad>', views.info_grados_universidad, name="grados_universidad"),
    path('consejos', views.consejos, name="consejos"),
    path('consejos/<blog>', views.consejos_blogs, name="animo_blogs"),
    path('contacto', views.contacto, name="contacto"),
    path('inicio-sesion', views.registro, name="registro"),
    path('foro', views.foro, name="foro")
]