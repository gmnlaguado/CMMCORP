# coding=utf-8
from kivy.network.urlrequest import UrlRequest
from declarations import class_declaration, querys
import json
from kivy.clock import mainthread


def uploadInformation():
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    verify = False
    timeout = 30
    debug = True

    url = 'http://corpmundialmujer.herokuapp.com/'
    end_point = 'payee'
    url += end_point
    tab = end_point
    method = 'POST'
    info_list = [json.dumps(dict(zip(querys.bringColumns(tab), list(pay)))) for pay in querys.bringData(tab)]
    for info in info_list:
        req = UrlRequest(url=url,
                         on_success=request_sucess,
                         on_failure=request_failure,
                         on_progress=request_progress,
                         on_error=request_error,
                         req_body=info,
                         req_headers=headers,
                         method=method,
                         verify=verify,
                         timeout=timeout,
                         debug=debug)
        req.wait()

    url = 'http://corpmundialmujer.herokuapp.com/'
    end_point = 'payeeProjects'
    url += end_point
    tab = end_point
    info_list = [json.dumps(dict(zip(querys.bringColumns(tab), list(pay)))) for pay in querys.bringData(tab)]
    for info in info_list:
        req = UrlRequest(url=url,
                         on_success=request_sucess,
                         on_failure=request_failure,
                         on_progress=request_progress,
                         on_error=request_error,
                         req_body=info,
                         req_headers=headers,
                         method=method,
                         verify=verify,
                         timeout=timeout,
                         debug=debug)
        req.wait()

    url = 'http://corpmundialmujer.herokuapp.com/'
    end_point = 'productionProfileDiag'
    url += end_point
    tab = end_point

    info_list = [json.dumps(dict(zip(querys.bringColumns(tab), list(pay)))) for pay in querys.bringData(tab)]
    for info in info_list:
        req = UrlRequest(url=url,
                         on_success=request_sucess,
                         on_failure=request_failure,
                         on_progress=request_progress,
                         on_error=request_error,
                         req_body=info,
                         req_headers=headers,
                         method=method,
                         verify=verify,
                         timeout=timeout,
                         debug=debug)
        req.wait()


@mainthread
def request_progress(req, current_size, total_size):
    class_declaration.MessagePopup('Request in progress').open()
    print(req, current_size, total_size)


@mainthread
def request_sucess(req, result):
    class_declaration.MessagePopup('Request sended sucessfully').open()
    tab = str(req.url).split('/')[-1]
    print(f'\n\nURL: {tab}\n\n')
    print(req, result)


@mainthread
def request_failure(req, result):
    class_declaration.MessagePopup('Request failed in sending process').open()
    print(req, result)


@mainthread
def request_error(req, result):
    class_declaration.MessagePopup(str(req.error)).open()
    print(req, result, req.error)
