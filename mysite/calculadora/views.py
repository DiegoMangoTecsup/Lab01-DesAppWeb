from django.http import HttpResponse

def sumar(request, a, b):
    resultado = int(a) + int(b)
    respuesta = f"La suma de {a} + {b} = {resultado}"
    return HttpResponse(respuesta)

def restar(request, a, b):
    resultado = int(a) - int(b)
    respuesta = f"La resta de {a} - {b} = {resultado}"
    return HttpResponse(respuesta)

def multiplicar(request, a, b):
    resultado = int(a) * int(b)
    respuesta = f"La multiplicación de {a} * {b} = {resultado}"
    return HttpResponse(respuesta)