from django.views.generic import *
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render,render_to_response
from Apps.Carrera.forms import *
from Apps.Carrera.models import *
from django.core import serializers
from django.http import HttpResponseBadRequest, HttpResponse, HttpRequest

def principal(request):
    return render(request, 'Sources/ver_principal.html')

class CiclistaCreate(CreateView):
    model = Ciclista
    form_class = form_ciclista
    template_name = 'Sources/form_ciclista.html'
    success_url = reverse_lazy('VerCiclistas')

def ciclistas_reg(request):
    lista = Ciclista.objects.all()
    return render_to_response('Sources/ver_registro_ciclistas.html', {'object_list': lista})

def ciclistas_edicion_reg(request,param):
    lista=Inscripcion.objects.filter(id_edicion=param)
    return render_to_response('Sources/ver_registro_ciclistas.html', {'object_list': lista})


def InscripcionList(request, param):
    lista = Inscripcion.objects.filter(id_edicion = param)
    return render_to_response('Sources/VerInscripciones', {'inscripciones': lista})

def carreras_reg(request):
    lista=Serie.objects.all()
    return render_to_response('Sources/ver_registro_carreras.html', {'carreras': lista})

class CarreraList(ListView):
    model = Serie
    template_name = 'Sources/ver_registro_carreras.html'

class reg_serie(CreateView):
    model = Serie
    form_class = form_serie
    template_name = 'Sources/form_carrera.html'
    success_url = reverse_lazy('RegistrarEdicion')

class reg_edicion(CreateView):
    model = Edicion
    form_class = form_etapa
    template_name = 'Sources/form_edicion.html'
    success_url = reverse_lazy('RegistrarEtapas')

class reg_etapas(CreateView):
    model = Etapa
    form_class = form_etapa
    template_name = 'Sources/form_ciclista.html'
    success_url = reverse_lazy('DetalleCarrera')

def ver_etapas(request, param):
    lista = Etapa.objects.filter(id_edicion = param)
    return render_to_response('Sources/ver_etapas.html', {'etapas': lista})

class reg_etapas(UpdateView):
    model = Etapa
    form_class = form_etapa
    template_name = 'Sources/form_ciclista.html'
    success_url = reverse_lazy('DetalleCarrera')



def DetalleCarrera(request, param):
    lista=[]
    serie_datos = Serie.objects.get(id=param)
    lista_ediciones = Edicion.objects.filter(id_serie=param)
    for edi in lista_ediciones:
        lista_etapas = Etapa.objects.filter(id_edicion=edi.id)
        lista.append(lista_etapas)
    return render_to_response('Sources/VerInscripciones.html', {'datos': serie_datos,'lista': lista})

def DetalleSerieEdicion(request,param):
    serie_datos = Serie.objects.get(id=param)
    edicion_datos = Edicion.objects.filter(id_serie=param)
    return render_to_response('Sources/ver_detalle_Carrera.html', {'datos': serie_datos, 'listae':edicion_datos})

def EdicionList(request, param):
    lista = Edicion.objects.filter(id_serie = param)
    return render_to_response('Sources/Ver', {'inscripciones': lista})

def buscar(request, param):
    lista = Serie.objects.filter(nombre_serie = param)

def search(request):
    # definimos el termino de busqueda
    q = request.POST['q']

    serie = Serie.objects.filter(nombre_serie__contains=q)

    # seleccionamos las columnas que deseamos obtener para el json
    serie_fields = ('id', 'nombre', 'descripcion')

    # to json!
    data = serializers.serialize('json', serie, fields=serie_fields)

    # eso es todo por hoy ^^
    return HttpResponse(data, content_type="application/json")
