from django.shortcuts import render
from prueba.models import prueba

def prue(request):
    if request.method=="GET":
        try:
            prueba = prueba.objects.values_list("texto", flat=True).get(username="prueba")
        except:
            prueba = "fallo."
    context = {'prueba': prueba }
    return render(request, 'prueba.html')