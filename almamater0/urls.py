from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('principal.urls')),
    path('forum/', include('core.urls')),
    path('', include('core.urls'))
]
handler404 = 'mysite.views.manage404'
handler500 = 'principal.views.manage500'
