from django.core.urlresolvers import reverse_lazy
from django.views.generic import *
from django.shortcuts import render,render_to_response, redirect
from Apps.Carrera.forms import *
from Apps.Carrera.models import Serie, Edicion, Etapa, Ciclista,Inscripcion
from django.http import HttpResponseRedirect


def principal(request):
    return render(request, 'Sources/ver_principal.html')

#Registrar en la base de datos
class reg_serie(CreateView):
    model = Serie
    form_class = form_serie
    template_name = 'Sources/form_carrera.html'
    success_url = reverse_lazy('VerCarreras')


class edit_serie(UpdateView):
    form_class = form_serie
    model =Serie
    template_name = 'Sources/form_carrera.html'
    success_url = reverse_lazy('VerCarreras')


class elim_serie(DeleteView):
    model = Serie
    template_name = 'Sources/elim_carrera.html'
    success_url = reverse_lazy('VerCarreras')

class reg_edicion(CreateView):
    model =Edicion
    form_class = reg_edicion
    template_name = 'Sources/form_edicion.html'
    success_url = reverse_lazy('VerCarreras')

class edit_edicion(UpdateView):
    form_class = form_edicion
    model = Edicion
    template_name = 'Sources/form_edicion.html'
    success_url = reverse_lazy('VerCarreras')

class elim_edicion(DeleteView):
    model = Edicion
    template_name = 'Sources/elim_edicion.html'
    success_url = reverse_lazy('VerCarreras')

class reg_etapas(CreateView):
    model = Etapa
    form_class = reg_etapa
    template_name = 'Sources/form_etapa.html'
    success_url = reverse_lazy('VerCarreras')

class edit_etapa(UpdateView):
    form_class = form_etapa
    model = Etapa
    template_name = 'Sources/form_etapa.html'
    success_url = reverse_lazy('VerCarreras')

class elim_etapa(DeleteView):
    model = Etapa
    template_name = 'Sources/elim_etapa.html'
    success_url = reverse_lazy('VerCarreras')

class reg_ciclista(CreateView):
    model = Ciclista
    form_class = form_ciclista
    template_name = 'Sources/form_ciclista.html'
    success_url = reverse_lazy('Inscribirse')

class reg_inscripcion2(CreateView):
    model = Inscripcion
    form_class = form_inscripcion
    template_name = 'Source/form_inscripcion.html'
    success_url = reverse_lazy('VerCarreras')

class inscripcion_list(ListView):
    model = Inscripcion
    template_name = 'Sources/ver_registro_inscritos.html'

#Visualizar los datos
def ver_carreras(request):
    lista = Serie.objects.all()
    return render(request, 'Sources/ver_registro_carreras.html', {'carreras': lista})
import json

def buscar_carrera(request):
    nombre = request.GET.get('nombre_carrera')
    lista = Serie.objects.filter(nombre_serie__icontains = nombre)
    return render_to_response('Sources/buscar_reg_carreras.html', {'carreras': lista})

def ver_ediciones_carrera(request,Serie_id):
    serie_datos = Serie.objects.get(id=Serie_id)
    edicion_lista = Edicion.objects.filter(id_serie_id=serie_datos)
    return render_to_response('Sources/ver_detalle_Carrera.html', {'datos': serie_datos, 'lista':edicion_lista})

def ver_etapas_edicion(request,Edicion_id):
    edicion_datos = Edicion.objects.get(id=Edicion_id)
    etapa_lista = Etapa.objects.filter(id_edicion_id=Edicion_id)
    return render_to_response('Sources/ver_etapas.html', {'datos': edicion_datos, 'lista':etapa_lista})

def ver_ciclistas(request):
    lista = Ciclista.objects.all()
    return render_to_response('Sources/ver_registro_ciclistas.html', {'ciclistas': lista})

def ver_inscripciones_edicion(request,Edicion_id):
    lista = Inscripcion.objects.filter(id_edicion_id = Edicion_id)
    return render_to_response('Sources/ver_inscritos.html', {'inscripciones': lista})

class reg_inscripcion(CreateView):
    model = Inscripcion
    template_name = 'Sources/reg_inscripcion.html'
    form_class = form_inscripcion
    second_form_class = form_ciclista
    success_url = reverse_lazy('VerCiclistas')

    def get_context_data(self, **kwargs):
        context = super(reg_inscripcion,self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context

    def post(self,request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            solicitud =form.save(commit=False)
            solicitud.id_ciclista = form2.save()
            solicitud.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form,form2=form2))


def gestionar_carreras(request):
    return render(request, 'Sources/form_carrera.html')

def carreras_disponibles(request):
    lista = Edicion.objects.filter( vigente = 'S')
    return render_to_response('Sources/ver_car_disponibles.html', {'ediciones': lista})
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
