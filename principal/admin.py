from django.contrib import admin
from principal.models import comentario, pregunta

class comentarioAdmin(admin.ModelAdmin):
    pass
admin.site.register(comentario, comentarioAdmin)

class preguntaAdmin(admin.ModelAdmin):
    pass
admin.site.register(pregunta, preguntaAdmin)