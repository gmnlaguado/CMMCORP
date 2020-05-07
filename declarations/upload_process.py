# coding=utf-8
from kivy.network.urlrequest import UrlRequest
from declarations import class_declaration, querys
import json
import encodings.idna


def uploadInformation():
    # url = 'http://corpmundialmujer.herokuapp.com/'
    # end_point = 'payee'
    # url += end_point
    #
    # method = 'POST'
    # headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    # verify = False
    # tab = 'payee'
    # timeout = 30
    # debug = True
    #
    # info_list = [json.dumps(dict(zip(querys.bringColumns(tab), list(pay)))) for pay in querys.bringData(tab)]
    # for info in info_list:
    #     req = UrlRequest(url=url,
    #                      on_success=request_sucess,
    #                      on_failure=request_failure,
    #                      on_progress=request_progress,
    #                      on_error=request_error,
    #                      req_body=info,
    #                      req_headers=headers,
    #                      method=method,
    #                      verify=verify,
    #                      timeout=timeout,
    #                      debug=debug)
    #
    # class_declaration.MessagePopup(f'Starting sending {len(info_list)} POST requests').open()

    # url = 'http://corpmundialmujer.herokuapp.com/'
    # req = UrlRequest(url=url,
    #                  on_success=request_sucess,
    #                  on_failure=request_failure,
    #                  on_progress=request_progress,
    #                  on_error=request_error)
    # class_declaration.MessagePopup('Request started').open()

    UrlRequest(
        url='http://corpmundialmujer.herokuapp.com/',
        on_error=lambda *args: print('error:', args),
        on_failure=lambda *args: print('fail:', args),
        on_redirect=lambda *args: print('redir:', args),
        on_success=lambda *args: print('success:', args)
    )


def request_progress(req, current_size, total_size):
    class_declaration.MessagePopup('Request in progress').open()
    print(req, current_size, total_size)


def request_sucess(req, result):
    class_declaration.MessagePopup('Request sended sucessfully').open()
    print(req, result)


def request_failure(req, result):
    class_declaration.MessagePopup('Request failed in sending process').open()
    print(req, result)


def request_error(req, result):
    class_declaration.MessagePopup(str(req.error)).open()
    print(req, result, req.error)
