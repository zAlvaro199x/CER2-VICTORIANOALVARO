from django.contrib import admin
from .models import Material, SolicitudDeRetiro

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)


@admin.register(SolicitudDeRetiro)
class SolicitudDeRetiroAdmin(admin.ModelAdmin):
    def display_fecha_retiro_estimada(self, obj):
        return obj.fecha_retiro_estimada
    display_fecha_retiro_estimada.short_description = 'Fecha Estimada Retiro'

    list_display = ('id', 'usuario', 'material', 'cantidad_estimada', 'display_fecha_retiro_estimada', 'estado', 'operario_asignado', 'fecha_solicitud')
    
    list_filter = ('estado', 'material', 'operario_asignado', 'fecha_solicitud')
    
    search_fields = ('usuario__username', 'material__nombre', 'direccion_retiro', 'estado')

    list_editable = ('estado', 'operario_asignado') 
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('usuario', 'material', 'cantidad_estimada', 'fecha_retiro_estimada', 'direccion_retiro')
        }),
        ('Gestión de Solicitud', {
            'fields': ('estado', 'operario_asignado', 'comentarios_operario'),
            'description': 'Campos para la gestión interna de la solicitud por parte de operarios o administradores.'
        }),
        ('Fechas', {
            'fields': ('fecha_solicitud',),
            'classes': ('collapse',),
        })
    )
    
    readonly_fields = ('fecha_solicitud', 'usuario')