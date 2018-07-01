from django.conf.urls import url
from Apps.Carrera.views import *



urlpatterns = (
    url(r'^Principal', principal, name='Principal'),
    url(r'^Registrarse', reg_ciclista.as_view(), name='Registrarse'),
    url(r'^Ciclistas', ver_ciclistas, name='VerCiclistas'),

    url(r'^DetalleCarrera/(?P<Serie_id>\d+)$', ver_ediciones_carrera, name='DetalleCarrera'),
    url(r'^AgregarCarrera/(?P<id_edicion>\d+)$', reg_serie.as_view(), name='AgregarCarrera'),

    url(r'^VerInscritos/(?P<id_edicion>\d+)$', ver_inscripciones_edicion, name='VerInscritos'),
    url(r'^VerEtapas/(?P<id_edicion>\d+)$', ver_etapas_edicion, name='VerEtapas'),
    url(r'^AgregarEdicion/(?P<id_edicion>\d+)$', reg_edicion.as_view(), name='AgregarEdicion'),

    # url(r'^EditarEdicion/(P?<id_edicion>\d+)$', editar_edicion,name='EditarEdicion'),
    # url(r'^EliminarEdicion/(P?<id_edicion>\d+)$', eliminar_edicion ,name='EliminarEdicion'),

    #    url(r'^VerEtapas/(P?<id_edicion>\d+)$', ver_etapas ,name='VerEtapas'),
    #    url(r'^AgregarEtapas',reg_etapas.as_view() ,name='AgregarEtapas'),
    #    url(r'^EditarEdicion/(P?<id_edicion>\d+)$', editar_etapa,name='EditarEdicion'),
    #    url(r'^EliminarEdicion/(P?<id_edicion>\d+)$', eliminar_etapa ,name='EliminarEdicion'),

    url(r'^Carreras/', ver_carreras, name='VerCarreras'),
    url(r'^Buscar$', buscar_carrera, name='BuscarCarrera'),
    url(r'^GestionarCarreras$',gestion, name ='GestionarCarreras'),
    url(r'^VerInscritosPorCarrera/(P?<id_edicion>\d+)$', ver_inscripciones_edicion, name='VerInscritosPorCarrera'),

    # url(r'^Carrera/search/', search, name='Buscar')
)