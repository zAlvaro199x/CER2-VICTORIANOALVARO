# Municipalidad/packet/urls.py

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views # Importa las vistas de autenticación de Django

urlpatterns = [
    path('admin/', admin.site.urls), # URL para el panel de administración
    path('', include('core.urls')), # URL para la pagina principal
    path('solicitudes/', include('solicitudes.urls')), # URL para la aplicación de solicitudes
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'), # URL para el inicio de sesión
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'), # URL para el cierre de sesión
]