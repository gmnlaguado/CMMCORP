# coding=utf-8
from declarations import querys
from kivy.network.urlrequest import UrlRequest
import json


def get_operarios():
    req = UrlRequest('http://190.145.94.92:5000/', got_json)

def got_json(req, result):
    print(result)
