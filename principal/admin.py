from django.contrib import admin
from principal.models import comentario, pregunta, falta

class comentarioAdmin(admin.ModelAdmin):
    pass
admin.site.register(comentario, comentarioAdmin)

class preguntaAdmin(admin.ModelAdmin):
    pass
admin.site.register(pregunta, preguntaAdmin)

class faltaAdmin(admin.ModelAdmin):
    pass
admin.site.register(falta, faltaAdmin)