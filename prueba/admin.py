from django.contrib import admin
from prueba.models import prueba

class pruebaAdmin(admin.ModelAdmin):
    pass
admin.site.register(prueba, pruebaAdmin)

