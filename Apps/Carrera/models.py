from django.db import models

class Serie(models.Model):
    nombre_serie = models.CharField(max_length=100, null=False)
    descripcion = models.CharField(max_length=300, null=False)

    def nom_serie(self):
        cadena1 = "{0}"
        return cadena1.format(self.nombre_serie)

    def __str__(self):
        return self.nom_serie()

class Edicion(models.Model):
    id_serie = models.ForeignKey(Serie, null=False, blank=True, on_delete=models.CASCADE)
    ano_edicion = models.IntegerField(null=False)
    descripcion = models.CharField(max_length=400, null=False)
    estados = (('S', 'Si'), ('N', 'No'))
    vigente = models.CharField(max_length=1, choices=estados, default='N')

    def nom_edicion(self):
        cadena2 = "{0} - {1}"
        return cadena2.format(self.id_serie, self.ano_edicion)

    def __str__(self):
        return self.nom_edicion()



class Etapa(models.Model):
    id_edicion = models.ForeignKey(Edicion, null=False, blank=True, on_delete=models.CASCADE)
    fecha = models.DateField()
    longitud = models.FloatField(null=False)
    pob_inicial = models.IntegerField(null=False)
    pob_final = models.IntegerField(null=False)
    pto_partida = models.CharField(max_length=200, null=False)
    pto_llegada = models.CharField(max_length=200, null=False)

    def nom_etapa(self):
        cadena3 = "{0} --> {1}"
        return cadena3.format(self.id_edicion, self.fecha)

    def __str__(self):
        return self.nom_etapa()

class Ciclista(models.Model):
    ape_pat = models.CharField(max_length=50, null=False)
    ape_mat = models.CharField(max_length=50, null=False)
    nombre = models.CharField(max_length=50, null=False)
    dni = models.CharField(max_length=8, null=False)
    direccion = models.CharField(max_length=100, null=False)
    sexos = (('M', 'Masculino'), ('F', 'Femenino'))
    sexo = models.CharField(max_length=1, choices=sexos, default='M')
    edad = models.IntegerField(null=False)
    peso = models.FloatField(null=False)
    talla = models.FloatField(null=False)

    def nom_ciclista(self):
        cadena4 = "{0} {1}, {2}"
        return cadena4.format(self.ape_pat, self.ape_mat, self.nombre)

    def __str__(self):
        return self.nom_ciclista()

class Inscripcion(models.Model):
    id_ciclista = models.ForeignKey(Ciclista,null=False, blank=True, on_delete=models.CASCADE)
    id_edicion = models.ForeignKey(Edicion,null=False, blank=True, on_delete=models.CASCADE)
    fecha_insc = models.DateTimeField(auto_now=True)

    def nom_inscripcion(self):
        cadena5 = "{0} // {1}"
        return cadena5.format(self.id_ciclista, self.id_edicion)

    def __str__(self):
        return self.nom_inscripcion()