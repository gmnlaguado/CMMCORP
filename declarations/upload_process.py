# coding=utf-8
from declarations import querys
from kivy.network.urlrequest import UrlRequest
import json


def uploadInformation():
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    url = 'https://httpbin.org/post'
    method = 'POST'

    tablas = querys.lista_de_tablas()

    for tab in tablas:
        res = querys.obtener_toda_info(tab)
        if len(res) > 0:
            res = json.dumps(dict(zip(querys.bringColumns(tab), list(res))))
            req = UrlRequest(url=url,
            on_success=request_sucess,
            on_progress=request_progress,
            req_body=res,
            req_headers=headers,
            method=method)

    #for tabs in tablas:
    #    querys.limpiar_tabla(tabs)


def request_sucess(req, result):
    print("\n\n\n Respuesta correcta \n\n\n")

def request_progress(req, current_size, total_size):
    print("\n\n\n Respuesta en proceso \n\n\n")
