from django.db import models 
from django.contrib.auth.models import User

class Material(models.Model): 
    codigo = models.CharField(max_length=10, unique=True) 
    nombre = models.CharField(max_length=100) 
    descripcion = models.TextField()

    def __str__(self): 
        return self.nombre 

    class Meta:
        verbose_name_plural = "Materiales"

class SolicitudDeRetiro(models.Model):
    ESTADOS_SOLICITUD = [ 
        ('PENDIENTE', 'Pendiente'),
        ('ASIGNADA', 'Asignada a Operario'),
        ('COMPLETADA', 'Completada'),
        ('RECHAZADA', 'Rechazada'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='solicitudes_creadas')
    material = models.ForeignKey(Material, on_delete=models.PROTECT) 
    cantidad_estimada = models.DecimalField(max_digits=5, decimal_places=2) 
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    fecha_retiro_estimada = models.DateField(null=True, blank=True) 
    direccion = models.CharField(max_length=255)
    estado = models.CharField(max_length=10, choices=ESTADOS_SOLICITUD, default='PENDIENTE') 
    operario_asignado = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='solicitudes_asignadas')
    comentarios_operario = models.TextField(blank=True, null=True)

    def __str__(self): 
        return f"Solicitud {self.pk} - {self.material.nombre} de {self.usuario.username} ({self.estado})" 

    class Meta:
        verbose_name_plural = "Solicitudes de Retiro" 
        ordering = ['-fecha_solicitud']