from django.contrib import admin
from principal.models import comentario

class comentarioAdmin(admin.ModelAdmin):
    pass
admin.site.register(comentario, comentarioAdmin)
