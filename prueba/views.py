from django.shortcuts import render

def prueba(request):
    if request.method=="GET":
        try:
            prueba = Prueba.objects.get(username="prueba")
        except:
            prueba = "fallo."
    context = {'prueba': prueba }
    return render(request, 'prueba.html')