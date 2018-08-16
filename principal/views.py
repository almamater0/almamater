from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import comentario

def inicio(request):
    return render(request, 'inicio.html')

#si la url es de tipo grados/asignatura, se pondra la template asignatura.html. la cosa es ahcer muchas templates analogas sobre eso
#para poner la info, simplemente subrie la plantilla a internet pra que elena pueda tocar
def info_grados(request, grado):
    template="grados/"+grado+".html"
    return render(request, template)


#aqui igual, pero con una universidad
def info_grados_universidad(request, grado, universidad):
    template="grados/"+grado+"_universidades/"+grado+"_"+universidad+".html"
    return render(request, template)

def consejos(request):
    return render(request, "consejos.html")

def consejos_blogs(request, blog):
    template="consejos/"+blog+".html"
    return render(request, template)

def contacto(request):
    return render(request,"contacto.html")

def gestion_comentario(request):
    if request.method=="POST":
        nuevo_comentario=request.POST.get('comentario_falta')
        crear_comentario=comentario.objects.create(texto_comentario=nuevo_comentario)
        crear_comentario.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def manage500(request):
    return render(request, "manageerror.html")

def manage404(request):
    return render(request, "manageerror.hmtl")

