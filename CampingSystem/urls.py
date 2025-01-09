from django.contrib import admin
from django.urls import path, include
from camping import views  # Importa las vistas de la aplicación camping

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Configura la raíz del sitio
    path('', include('camping.urls')),  # Incluye las URLs de la aplicación camping
]
