def roles_context(request):
    es_operario = False
    es_administrador_custom = False

    if request.user.is_authenticated:
        if request.user.is_superuser:
            es_operario = True
            es_administrador_custom = True
        elif request.user.is_staff and request.user.groups.filter(name='Operarios').exists():
            es_operario = True

    return {
        'es_operario': es_operario,
        'es_administrador_custom': es_administrador_custom,
    }