import requests
import json

def listar_jurisprudencia(buscar):
    data = {
    "page": 1,
    "pageSize": 10,
    "orden": "nuevo",
    "search": buscar
    }      

    url = 'https://www.buscadorambiental.cl/buscador-api/jurisprudencias/list'  # Reemplaza con la URL correcta de tu API
    response = requests.post(url, data=data)

