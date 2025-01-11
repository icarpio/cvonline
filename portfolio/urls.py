
from django.contrib import admin
from django.urls import path
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('landingpage.urls')),  # Redirige la raíz al archivo de URLs de 'miapp'
]