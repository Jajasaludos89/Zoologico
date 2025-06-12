import os
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Evento, Patrocinador, EventoPatrocinador

#Tabla Evento

def listarEvento(request):
    eventos = Evento.objects.all()
    return render(request, "listarEvento.html", {'eventos': eventos})

def nuevoEvento(request):
    return render(request, "nuevoEvento.html")

def guardarEvento(request):
    nombre = request.POST["nombre"]
    fecha = request.POST["fecha"]
    descripcion = request.POST["descripcion"]

    foto_evento = request.FILES.get("foto_evento")
    pdf_programa = request.FILES.get("pdf_programa")

    Evento.objects.create(
        nombre=nombre,
        fecha=fecha,
        descripcion=descripcion,
        foto_evento=foto_evento,
        pdf_programa=pdf_programa
    )
    messages.success(request, "Evento GUARDADO exitosamente")
    return redirect('/listarEvento')

def eliminarEvento(request, id):
    evento = Evento.objects.get(id=id)
    if evento.foto_evento and os.path.isfile(evento.foto_evento.path):
        os.remove(evento.foto_evento.path)
    if evento.pdf_programa and os.path.isfile(evento.pdf_programa.path):
        os.remove(evento.pdf_programa.path)
    evento.delete()
    messages.success(request, "Evento ELIMINADO exitosamente")
    return redirect('/listarEvento')

def editarEvento(request, id):
    evento = Evento.objects.get(id=id)
    return render(request, "editarEvento.html", {'evento': evento})

def procesarEdicionEvento(request):
    id = request.POST["id"]
    nombre = request.POST["nombre"]
    fecha = request.POST["fecha"]
    descripcion = request.POST["descripcion"]

    foto_evento = request.FILES.get("foto_evento")
    pdf_programa = request.FILES.get("pdf_programa")

    evento = Evento.objects.get(id=id)
    evento.nombre = nombre
    evento.fecha = fecha
    evento.descripcion = descripcion

    if foto_evento:
        if evento.foto_evento and os.path.isfile(evento.foto_evento.path):
            os.remove(evento.foto_evento.path)
        evento.foto_evento = foto_evento

    if pdf_programa:
        if evento.pdf_programa and os.path.isfile(evento.pdf_programa.path):
            os.remove(evento.pdf_programa.path)
        evento.pdf_programa = pdf_programa

    evento.save()
    messages.success(request, "Evento ACTUALIZADO exitosamente")
    return redirect('/listarEvento')

#Tabla de Patrocinador

def listarPatrocinador(request):
    patrocinadores = Patrocinador.objects.all()
    return render(request, "listarPatrocinador.html", {'patrocinadores': patrocinadores})

def nuevoPatrocinador(request):
    return render(request, "nuevoPatrocinador.html")

def guardarPatrocinador(request):
    nombre = request.POST["nombre"]
    industria = request.POST["industria"]
    logo_patrocinador = request.FILES.get("logo_patrocinador")

    Patrocinador.objects.create(
        nombre=nombre,
        industria=industria,
        logo_patrocinador=logo_patrocinador
    )
    messages.success(request, "Patrocinador GUARDADO exitosamente")
    return redirect('/listarPatrocinador')

def eliminarPatrocinador(request, id):
    patrocinador = Patrocinador.objects.get(id=id)
    if patrocinador.logo_patrocinador and os.path.isfile(patrocinador.logo_patrocinador.path):
        os.remove(patrocinador.logo_patrocinador.path)
    patrocinador.delete()
    messages.success(request, "Patrocinador ELIMINADO exitosamente")
    return redirect('/listarPatrocinador')

def editarPatrocinador(request, id):
    patrocinador = Patrocinador.objects.get(id=id)
    return render(request, "editarPatrocinador.html", {'patrocinador': patrocinador})

def procesarEdicionPatrocinador(request):
    id = request.POST["id"]
    nombre = request.POST["nombre"]
    industria = request.POST["industria"]
    logo_patrocinador = request.FILES.get("logo_patrocinador")

    patrocinador = Patrocinador.objects.get(id=id)
    patrocinador.nombre = nombre
    patrocinador.industria = industria

    if logo_patrocinador:
        if patrocinador.logo_patrocinador and os.path.isfile(patrocinador.logo_patrocinador.path):
            os.remove(patrocinador.logo_patrocinador.path)
        patrocinador.logo_patrocinador = logo_patrocinador

    patrocinador.save()
    messages.success(request, "Patrocinador ACTUALIZADO exitosamente")
    return redirect('/listarPatrocinador')

#Tabla EventoPatrocinador

def listarEventoPatrocinador(request):
    eventos_patrocinadores = EventoPatrocinador.objects.all()
    return render(request, "listarEventoPatrocinador.html", {'eventos_patrocinadores': eventos_patrocinadores})

def nuevoEventoPatrocinador(request):
    eventos = Evento.objects.all()
    patrocinadores = Patrocinador.objects.all()
    return render(request, "nuevoEventoPatrocinador.html", {
        'eventos': eventos,
        'patrocinadores': patrocinadores
    })

def guardarEventoPatrocinador(request):
    if request.method == 'POST':
        evento_id = request.POST["evento_id"]
        patrocinador_id = request.POST["patrocinador_id"]
        aporte_economico = request.POST["aporte_economico"]
        pdf_contrato = request.FILES.get("pdf_contrato")

        evento = Evento.objects.get(id=evento_id)
        patrocinador = Patrocinador.objects.get(id=patrocinador_id)

        EventoPatrocinador.objects.create(  #la actualizacion se hace atraves del uso de create
            evento=evento,
            patrocinador=patrocinador,
            aporte_economico=aporte_economico,
            pdf_contrato=pdf_contrato
        )

        messages.success(request, "Patrocinio GUARDADO exitosamente")
    return redirect('/listarEventoPatrocinador')

def eliminarEventoPatrocinador(request, id):
    ep = EventoPatrocinador.objects.get(id=id)
    if ep.pdf_contrato and os.path.isfile(ep.pdf_contrato.path):
        os.remove(ep.pdf_contrato.path)
    ep.delete()
    messages.success(request, "Patrocinio ELIMINADO exitosamente")
    return redirect('/listarEventoPatrocinador')

def editarEventoPatrocinador(request, id):
    ep = EventoPatrocinador.objects.get(id=id)
    eventos = Evento.objects.all()
    patrocinadores = Patrocinador.objects.all()
    return render(request, "editarEventoPatrocinador.html", {
        'ep': ep,
        'eventos': eventos,
        'patrocinadores': patrocinadores
    })

def procesarEdicionEventoPatrocinador(request):
    if request.method == 'POST':
        id = request.POST["id"]
        evento_id = request.POST["evento_id"]
        patrocinador_id = request.POST["patrocinador_id"]
        aporte_economico = request.POST["aporte_economico"]
        pdf_contrato = request.FILES.get("pdf_contrato")

        ep = EventoPatrocinador.objects.get(id=id)
        ep.evento = Evento.objects.get(id=evento_id)
        ep.patrocinador = Patrocinador.objects.get(id=patrocinador_id)
        ep.aporte_economico = aporte_economico

        if pdf_contrato:
            if ep.pdf_contrato and os.path.isfile(ep.pdf_contrato.path):
                os.remove(ep.pdf_contrato.path)
            ep.pdf_contrato = pdf_contrato

        ep.save()  #aqui tambien se hace la actualizacion pero al momento de editar
        messages.success(request, "Patrocinio ACTUALIZADO exitosamente")

    return redirect('/listarEventoPatrocinador')

