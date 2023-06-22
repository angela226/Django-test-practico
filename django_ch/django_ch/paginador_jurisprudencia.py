from django.db import models
from jurisprudencia import Jurisprudencia

class PaginadorJurisprudencia(models.Model):
    totalitems = models.TextField()
    totalpages = models.TextField()
    currentpage = models.TextField()
    jurisprudencias = models.ManyToManyField(Jurisprudencia)

