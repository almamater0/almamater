from django.shortcuts import render
from prueba.models import p

def prue(request):
    prueba = p.objects.values_list("texto", flat=True).get(username="prueba")
    context = {'prueba': prueba }
    return render(request, 'prueba.html', context)