from django.urls import path
from . import views

app_name = 'solicitudes'

urlpatterns = [
    path('', views.index, name='index'),
    path('crear/', views.crear_solicitud, name='crear_solicitud'),
    path('dashboard_operario/', views.dashboard_operario, name='dashboard_operario'),
]