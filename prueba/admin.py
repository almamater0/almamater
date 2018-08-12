from django.contrib import admin
from prueba.models import p

class pAdmin(admin.ModelAdmin):
    pass
admin.site.register(p, pAdmin)

