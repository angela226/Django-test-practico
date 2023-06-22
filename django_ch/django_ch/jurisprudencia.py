from django.db import models
from valores_jurisprudencia import ValoresJurisprudencia

class Jurisprudencia(models.Model):
    id = models.AutoField(primary_key=True)
    tipocausa = models.TextField()
    rol = models.TextField()
    caratula = models.TextField()
    nombreproyecto =  models.TextField()
    fechasentencia =  models.DateField()
    descriptores =  models.TextField()
    linksentencia =  models.TextField()
    urlsentencia =  models.TextField()
    activo =  models.BooleanField()
    tribunal =  models.TextField()
    valores = models.ManyToManyField(ValorJurisprudencia)

    