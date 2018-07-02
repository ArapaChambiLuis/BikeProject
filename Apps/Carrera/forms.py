from Apps.Carrera.models import *
from django import forms

class form_serie(forms.ModelForm):
    class Meta:
        model = Serie
        fields = [
            'nombre_serie', 'descripcion'
        ]
        labels = {
            'nombre_serie': 'Nombre de carrera',
            'descripcion': 'Descripcion'
        }
        widgets = {
            'nombre_serie' : forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion' : forms.TextInput(attrs={'class': 'form-control'}),
        }

class reg_edicion(forms.ModelForm):
    class Meta:
        model = Edicion
        fields = [
            'id_serie', 'ano_edicion', 'descripcion', 'vigente'
        ]

        labels = {
            'id_serie': 'Nombre de carrera',
            'ano_edicion': 'Año de edicion',
            'descripcion' : 'Descripcion',
            'vigente' : 'Vigente'
        }

        widgets = {
            'id_serie': forms.Select(attrs={'class': 'form-control'}),
            'ano_edicion': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'vigente': forms.Select(attrs={'class': 'form-control'}),
        }

class form_edicion(forms.ModelForm):
    class Meta:
        model = Edicion
        fields = [
            'id_serie', 'ano_edicion', 'descripcion', 'vigente'
        ]

        labels = {
            'id_serie': 'Nombre de carrera',
            'ano_edicion': 'Año de edicion',
            'descripcion' : 'Descripcion',
            'vigente' : 'Vigente'
        }

        widgets = {
            'id_serie': forms.HiddenInput(attrs={'class': 'form-control'}),
            'ano_edicion': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'vigente': forms.Select(attrs={'class': 'form-control'}),
        }


class reg_etapa(forms.ModelForm):
    class Meta:
        model = Etapa
        fields = [
            'id_edicion', 'fecha', 'longitud', 'pob_inicial', 'pob_final', 'pto_partida', 'pto_llegada'
        ]

        labels = {
            'id_edicion': 'Nombre de edicion',
            'fecha': 'Fecha',
            'longitud': 'Longitud',
            'pob_inicial': 'Poblacion inicial',
            'pob_final': 'Poblacion final',
            'pto_partida': 'Punto de partida',
            'pto_llegada' : 'Punto de llegada'
        }

        widgets = {
            'id_edicion': forms.Select(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control'}),
            'longitud': forms.TextInput(attrs={'class': 'form-control'}),
            'pob_inicial': forms.TextInput(attrs={'class': 'form-control'}),
            'pob_final': forms.TextInput(attrs={'class': 'form-control'}),
            'pto_partida': forms.TextInput(attrs={'class': 'form-control'}),
            'pto_llegada': forms.TextInput(attrs={'class': 'form-control'})
        }

class form_etapa(forms.ModelForm):
    class Meta:
        model = Etapa
        fields = [
            'id_edicion', 'fecha', 'longitud', 'pob_inicial', 'pob_final', 'pto_partida', 'pto_llegada'
        ]

        labels = {
            'id_edicion': 'Nombre de edicion',
            'fecha': 'Fecha',
            'longitud': 'Longitud',
            'pob_inicial': 'Poblacion inicial',
            'pob_final': 'Poblacion final',
            'pto_partida': 'Punto de partida',
            'pto_llegada' : 'Punto de llegada'
        }

        widgets = {
            'id_edicion': forms.HiddenInput(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control'}),
            'longitud': forms.TextInput(attrs={'class': 'form-control'}),
            'pob_inicial': forms.TextInput(attrs={'class': 'form-control'}),
            'pob_final': forms.TextInput(attrs={'class': 'form-control'}),
            'pto_partida': forms.TextInput(attrs={'class': 'form-control'}),
            'pto_llegada': forms.TextInput(attrs={'class': 'form-control'})
        }

class form_ciclista(forms.ModelForm):
    class Meta:
        model = Ciclista
        fields = [
            'ape_pat', 'ape_mat', 'nombre', 'dni', 'direccion', 'sexo', 'edad', 'peso', 'talla'
        ]

        labels = {
            'ape_pat': 'Apellido paterno',
            'ape_mat': 'Apellido materno',
            'nombre': 'Nombre',
            'dni': 'DNI',
            'direccion' : 'Direccion',
            'sexo' : 'Sexo',
            'edad' : 'Edad',
            'peso' : 'Peso',
            'talla' : 'Talla'
        }

        widgets = {
            'ape_pat': forms.TextInput(attrs={'class': 'form-control'}),
            'ape_mat': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'dni': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'sexo': forms.Select(attrs={'class': 'form-control'}),
            'edad': forms.TextInput(attrs={'class': 'form-control'}),
            'peso': forms.TextInput(attrs={'class': 'form-control'}),
            'talla': forms.TextInput(attrs={'class': 'form-control'})
        }

class form_inscripcion(forms.ModelForm):
    class Meta:
        model = Inscripcion
        fields = [
            'id_edicion'
        ]
        labels = {
            'id_edicion' : 'Carrera a la que desea participar'
        }
        widgets = {
            'id_edicion': forms.Select(attrs={'class': 'form-control'})
        }