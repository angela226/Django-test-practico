import requests
import json
from jurisprudencia import Jurisprudencia
from paginador_jurisprudencia import PaginadorJurisprudencia
from valores_jurisprudencia import ValorJurisprudencia

def listar_jurisprudencia(buscar):
    data = {
    "page": 1,
    "pageSize": 10,
    "orden": "nuevo",
    "search": buscar
    }      

    url = 'https://www.buscadorambiental.cl/buscador-api/jurisprudencias/list'  # Reemplaza con la URL correcta de tu API
    response = requests.post(url, data=data)
    if response.status_code == 200:
        response_json = response.json()
        paginadorJurisprudencia = PaginadorJurisprudencia(response_json["totalItems"], response_json["totalPages"], response_json["currentPage"], response_json["jurisprudencias"])
        jurisprudencias_data = response_json["jurisprudencias"]
        jurisprudencias = []
        for jurisprudencia_data in jurisprudencias_data:
            objetoJurisprudencia = Jurisprudencia(jurisprudencia_data["id"], jurisprudencia_data["tipoCausa"], jurisprudencia_data["rol"], jurisprudencia_data["caratula"], jurisprudencia_data["nombreProyecto"], jurisprudencia_data["fechaSentencia"], jurisprudencia_data["descriptores"], jurisprudencia_data["linkSentencia"], jurisprudencia_data["urlSentencia"], jurisprudencia_data["activo"], jurisprudencia_data["tribunal"], jurisprudencia_data["valores"])
            jurisprudencias.append(objetoJurisprudencia)
    else:
        print("Error")

