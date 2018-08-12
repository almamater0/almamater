from django.shortcuts import render
from prueba.models import prueba

def prueba(request):
    if request.method=="GET":
        try:
            prueba = Prueba.objects.get(username="prueba")
        except:
            prueba = "fallo."
    context = {'prueba': prueba }
    return render(request, 'prueba.html')