from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import PerfilUsuario

# integrar el modelo PerfilUsuario en la pagina de administración de User.
class PerfilUsuarioInline(admin.StackedInline):
    model = PerfilUsuario
    can_delete = False 
    verbose_name_plural = 'perfil'

# Extiende la administración de usuarios predeterminada de Django.
class CustomUserAdmin(UserAdmin):
    inlines = (PerfilUsuarioInline,)

# Desregistra el modelo User de la administración predeterminada de Django
admin.site.unregister(User)

# Registra el modelo User con nuestra clase de administración personalizada
# la página de usuarios en el panel de administración mostrará los campos de PerfilUsuario.
admin.site.register(User, CustomUserAdmin)