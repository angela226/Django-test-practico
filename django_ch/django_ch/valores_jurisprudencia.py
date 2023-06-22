from django.db import models


class ValorJurisprudencia(models.Model):
    id =  models.AutoField(primary_key=True)
    idparametro = idparametro
    iditemlista = iditemlista
    valor = models.TextField()
    parametro = models.TextField()
    item = models.TextField()
