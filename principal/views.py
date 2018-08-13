from django.shortcuts import render

def inicio(request):
    return render(request, 'inicio.html')

def info_grados(request, grado):
    template=grado+".html"
    return render(request, template)