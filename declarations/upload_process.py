# coding=utf-8
from declarations import querys
from kivy.network.urlrequest import UrlRequest
from declarations import class_declaration
from codes import snippets
from kivy.clock import mainthread
import json

url_base = 'http://192.168.20.36:5000/'
def get_operarios():
    url = url_base + 'obtener_operarios'
    method = "POST"
    req_body = "req_body"
    req = UrlRequest(url, 
                    method = method, 
                    req_body = req_body, 
                    on_success=operarios_respuesta, 
                    on_progress=operarios_progreso)

def operarios_respuesta(*args):
    snippets.actualizando_operarios(args[1])

def operarios_progreso(*args):
    print('\t',args[0].resp_status)


def get_operarios_proyectos():
    url = 'http://192.168.20.36:5000/obtener_operarios_proyectos'
    method = "POST"
    req_body = "req_body"
    req = UrlRequest(url, 
                    method = method, 
                    req_body = req_body, 
                    on_success=on_success_get_op, 
                     on_progress=on_progress_get_op)

def on_success_get_op(*args):
    snippets.actualizando_operarios_proyectos(args[1])

def on_progress_get_op(*args):
    #print('\t',args[0].resp_status)
    pass


def uploadInformation(*args):
    url = url_base + str(args[0])
    method = "POST"
    result = querys.bringData(str(args[0]))
    cols = querys.bringColumns(str(args[0]))

    req_header = {
        'Content-Type': 'application/json'
    }
    req_body = json.dumps({
        str(args[0]): result,
        'cols': cols

    })
    req = UrlRequest(url,
                     method=method,
                     req_headers=req_header,
                     req_body=req_body,
                     on_success=upload_success,
                     on_progress=upload_progress)


def upload_success(req, result):
    pass

def upload_progress(*args):
    pass

def reload_db(*args):
    url = url_base + 'obtener_datos/' + str(args[0])
    req = UrlRequest(url,
                     on_success=on_reload_success,
                     on_progress=on_reload_progress)

def on_reload_success(req, result):
    snippets.reload_data(result)


def on_reload_progress(*args):
    #print('\t', args[0].resp_status)
    pass
