from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login

from .forms import UserRegistrationForm 
from .models import PerfilUsuario 

from django.db.models import Count, Sum 
from django.db.models.functions import TruncMonth
from solicitudes.models import SolicitudDeRetiro, Material 

def home(request):
    materiales = Material.objects.all()

    #obtener el número de solicitudes por mes
    solicitudes_por_mes_query = SolicitudDeRetiro.objects \
        .annotate(month=TruncMonth('fecha_solicitud')) \
        .values('month') \
        .annotate(count=Count('id')) \
        .order_by('month') 
    
    #Formatea los datos
    solicitudes_mes_formateadas = [] 
    for item in solicitudes_por_mes_query: 
        nombre_mes = item['month'].strftime('%B') 
        nombre_mes = nombre_mes.capitalize() 
        solicitudes_mes_formateadas.append({ 
            'mes': f"{nombre_mes} {item['month'].year}",
            'cantidad': item['count']
        })

    materiales_mas_reciclados = SolicitudDeRetiro.objects \
        .values('material__nombre') \
        .annotate(total_cantidad=Sum('cantidad_estimada')) \
        .order_by('-total_cantidad')[:5] # Ordena de mayor a menor y toma los primeros 5

    context = {
        'materiales': materiales,
        'solicitudes_por_mes': solicitudes_mes_formateadas, 
        'materiales_mas_reciclados': materiales_mas_reciclados, 
    }
    return render(request, 'home.html', context) 



def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False) 
            user.set_password(form.cleaned_data['password']) 
            user.first_name = form.cleaned_data['first_name']
            user.save() 

            perfil = user.perfilusuario 
            perfil.direccion = form.cleaned_data['direccion']
            perfil.telefono = form.cleaned_data['telefono'] 
            perfil.save()

            username = form.cleaned_data.get('username') 
            messages.success(request, f'¡Cuenta creada para {username}! Ahora puedes iniciar sesión.') 

            login(request, user) 
            return redirect('core:home') 
        else: 
            messages.error(request, 'Hubo un error al registrar tu cuenta. Por favor, verifica los datos.') 
    else: 
        form = UserRegistrationForm() 

    context = { 
        'form': form
    }
    return render(request, 'registration/register.html', context)