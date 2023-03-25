from django.http import HttpResponse

def index(request):
    return HttpResponse("Desde la visa de encuestas!")

def detalle(request,pregunta_id):
    return HttpResponse('Estas viendo la pregunta %s' % pregunta_id)