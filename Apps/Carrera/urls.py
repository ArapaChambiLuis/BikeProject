from django.conf.urls import url
from Apps.Carrera.views import *

urlpatterns = (
    url(r'^Principal', principal, name='Principal'),
    url(r'^Ciclistas', ver_ciclistas, name='VerCiclistas'),
    url(r'^DetalleCarrera/(?P<Serie_id>\d+)$', ver_ediciones_carrera, name='DetalleCarrera'),

    url(r'^AgregarCarrera$', reg_serie.as_view(), name='AgregarCarrera'),
    url(r'^EditarCarrera/(?P<pk>\d+)$', edit_serie.as_view(),name='EditarCarrera'),
    url(r'^EliminarCarrera/(?P<pk>\d+)$', elim_serie.as_view() ,name='EliminarCarrera'),
    url(r'^VerInscritos/(?P<Edicion_id>\d+)$', ver_inscripciones_edicion, name='VerInscritos'),
    url(r'^VerEtapas/(?P<Edicion_id>\d+)$', ver_etapas_edicion, name='VerEtapas'),

    url(r'^AgregarEdicion/(?P<Serie_id>\d+)$', reg_edicion.as_view(), name='AgregarEdicion'),
    url(r'^EditarEdicion/(?P<pk>\d+)$', edit_edicion.as_view(),name='EditarEdicion'),
    url(r'^EliminarEdicion/(?P<pk>\d+)$', elim_edicion.as_view() ,name='EliminarEdicion'),

    url(r'^VerEtapas/(?P<id_edicion>\d+)$', ver_etapas_edicion ,name='VerEtapas'),
    url(r'^VerEtapas/AgregarEtapas$',reg_etapas.as_view() ,name='AgregarEtapas'),
    url(r'^EditarEtapa/(?P<pk>\d+)$', edit_etapa.as_view(),name='EditarEtapa'),
    url(r'^EliminarEtapa/(?P<pk>\d+)$', elim_etapa.as_view() ,name='EliminarEtapa'),

    url(r'^Carreras', ver_carreras, name='VerCarreras'),
    url(r'^Buscar', buscar_carrera, name='BuscarCarrera'),
    url(r'^Disp',carreras_disponibles, name ='Disponibles'),

    url(r'^AgregarInscripcion',reg_inscripcion.as_view(), name ='Inscribirse'),
    url(r'^VerInscritosPorCarrera/(?P<id_edicion>\d+)', ver_inscripciones_edicion, name='VerInscritosPorCarrera'),

    # url(r'^Carrera/search/', search, name='Buscar')
)