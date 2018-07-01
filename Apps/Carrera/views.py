from django.core.urlresolvers import reverse_lazy
from django.views.generic import *
from django.shortcuts import render,render_to_response, redirect
from Apps.Carrera.forms import *
from Apps.Carrera.models import Serie, Edicion, Etapa, Ciclista,Inscripcion

def principal(request):
    return render(request, 'Sources/ver_principal.html')

#Registrar en la base de datos
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

class reg_ciclista(CreateView):
    model = Ciclista
    form_class = form_ciclista
    template_name = 'Sources/form_ciclista.html'
    success_url = reverse_lazy('VerCiclistas')

#Visualizar los datos
def ver_carreras(request):
    lista = Serie.objects.all()
    return render(request, 'Sources/ver_registro_carreras.html', {'carreras': lista})

def ver_ediciones_carrera(param):
    serie_datos = Serie.objects.get(id=param)
    edicion_lista = Edicion.objects.filter(id_serie=serie_datos)
    return render_to_response('Sources/ver_detalle_Carrera.html', {'datos': serie_datos, 'listae':edicion_lista})

def ver_etapas_edicion(param):
    edicion_datos = Edicion.objects.get(id=param)
    etapa_lista = Etapa.objects.filter(id_edicion=edicion_datos)
    return render_to_response('Sources/ver_detalle_Carrera.html', {'datos': edicion_datos, 'listae':etapa_lista})

def ver_ciclistas(request):
    lista = Ciclista.objects.all()
    return render_to_response('Sources/ver_registro_ciclistas.html', {'ciclistas': lista})

def ver_inscripciones_edicion(param):
    lista = Inscripcion.objects.filter(id_edicion = param)
    return render_to_response('Sources/VerInscripciones', {'inscripciones': lista})

def gestionar_carreras(request):
    return render(request, 'Sources/form_carrera.html')


#----Otros
def DetalleCarrera(request, param):
    lista=[]
    serie_datos = Serie.objects.get(id=param)
    lista_ediciones = Edicion.objects.filter(id_serie=serie_datos)
    for edi in lista_ediciones:
        lista_etapas = Etapa.objects.filter(id_edicion=edi)
        lista.append(lista_etapas)
    return render_to_response('Sources/VerInscripciones.html', {'datos': serie_datos,'lista': lista})


def EdicionList(request, param):
    lista = Edicion.objects.filter(id_serie = param)
    return render_to_response('Sources/Ver', {'inscripciones': lista})

def buscar(request, param):
    lista = Serie.objects.filter(nombre_serie = param)

def gestion(request):
    if request.method == 'POST':
        form = form_serie(request.POST)
        if form.is_valid():
            form.save()
        return redirect('Sources:VerCarreras')
    else:
        form = form_serie()
        return render(request, 'Sources/form_carrera.html', {'form': form})
