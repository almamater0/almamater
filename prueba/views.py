from django.shortcuts import render
from prueba.models import p

def prue(request):
    if request.method=="GET":
        try:
            prueba = p.objects.values_list("texto", flat=True).get(username="prueba")
        except:
            prueba = "fallo."
    context = {'prueba': prueba }
    return render(request, 'prueba.html')