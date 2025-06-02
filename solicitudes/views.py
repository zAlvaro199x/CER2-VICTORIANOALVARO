from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Material, SolicitudDeRetiro 
from .forms import SolicitudDeRetiroForm


@login_required
def index(request):
    solicitudes = SolicitudDeRetiro.objects.filter(usuario=request.user).order_by('-fecha_solicitud')
    materiales = Material.objects.all()
    context = {
        'solicitudes': solicitudes,
        'materiales': materiales
    }
    return render(request, 'index.html', context)


@login_required
def crear_solicitud(request):
    if request.method == 'POST':
        form = SolicitudDeRetiroForm(request.POST)
        if form.is_valid():
            solicitud = form.save(commit=False)
            solicitud.usuario = request.user
            solicitud.save()
            messages.success(request, '¡Tu solicitud de retiro ha sido creada exitosamente!')
            return redirect('solicitudes:index') 
        else:
            messages.error(request, 'Hubo un error al crear tu solicitud. Por favor, verifica los datos.')
    else:
        form = SolicitudDeRetiroForm()

    context = {
        'form': form
    }
    return render(request, 'crear_solicitud.html', context)



def es_operario(user):
    return user.is_staff and user.groups.filter(name='Operarios').exists()

@login_required
@user_passes_test(es_operario, login_url='/admin/login/')
def dashboard_operario(request):
    solicitudes_asignadas = SolicitudDeRetiro.objects.filter(operario_asignado=request.user).order_by('-fecha_solicitud')

    if request.method == 'POST':
        solicitud_id = request.POST.get('solicitud_id')
        estado_nuevo = request.POST.get('estado_nuevo')
        comentarios_nuevo = request.POST.get('comentarios_operario')

        solicitud = get_object_or_404(SolicitudDeRetiro, id=solicitud_id, operario_asignado=request.user)

        if estado_nuevo and estado_nuevo in [choice[0] for choice in SolicitudDeRetiro.ESTADOS_SOLICITUD]:
            solicitud.estado = estado_nuevo

        if comentarios_nuevo is not None: 
            solicitud.comentarios_operario = comentarios_nuevo 

        solicitud.save()
        messages.success(request, f'Solicitud {solicitud.id} actualizada correctamente.')
        return redirect('solicitudes:dashboard_operario')

    context = {
        'solicitudes_asignadas': solicitudes_asignadas,
        'ESTADOS_SOLICITUD': SolicitudDeRetiro.ESTADOS_SOLICITUD 
    }
    return render(request, 'dashboard_operario.html', context)