# coding=utf-8
from declarations import querys
from kivy.network.urlrequest import UrlRequest
import json


def uploadInformation():
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    url = 'http://190.145.94.92:5000/'
    method = 'POST'
    tablas = querys.lista_de_tablas()
    for tab in tablas:
        res = querys.obtener_toda_info(tab)
        if len(res) > 0:
            full_url = url + tab
            for individual_res in res:
                res_dict = {}
                for idx, indv in enumerate(individual_res):
                    res_dict[str(idx+1)] = indv
                res_dict = json.dumps(res_dict, indent=4)
                print(full_url, '\n', res_dict, '\n\n')
                req = UrlRequest(url=full_url,
                                 on_success=request_sucess,
                                 on_progress=request_progress,
                                 req_body=res_dict,
                                 req_headers=headers,
                                 method=method)
            print("\n\n\n")


def request_sucess(req, result):
    print(f"\n\nrequest_sucess\n\n")


def request_progress(req, current_size, total_size):
    print(f"\n\nrequest_progress\n\n")

   # for tab in tablas:
    #    full_url = url+tab
    #    res = querys.obtener_toda_info(tab)
    #    print(full_url)
    #    if len(res) > 0:
    #        print(res[0])
    #        res = json.dumps({res[0]})
     #       req = UrlRequest(url=full_url,
    #        on_success=request_sucess,
    #        on_progress=request_progress,
    #        req_body=res,
    #        req_headers=headers,
     #       method=method)



    #for tabs in tablas:
    #    querys.limpiar_tabla(tabs)


#def request_sucess(req, result):
 #   resultado = result['data']
  #  resultado = resultado.split('": [')
  #  print(f"\n\n\n{resultado[0][2:]}\n{resultado[1][:-2]}\n\n")


#def request_progress(req, current_size, total_size):
  #  print(f"\n\n\n Respuesta en proceso {req}\n\n\n")
