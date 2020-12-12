# coding=utf-8
import re
import datetime


def username(username):
    if re.search(r"^[a-zA-Z0-9]+$", username) is not None and len(username) > 0:
        return True
    return False


def password(password):
    if re.search(r"[^\w,.]", password) is None and len(password) > 0:
        return True
    return False


def date(date):
    if re.search(r'^\d{2}[/]\d{2}[/]\d{4}$', date) is not None:
        date = date.split('/')
        if 0 <= int(date[0]) <= 31:
            if 0 <= int(date[1]) <= 12:
                if 1900 <= int(date[2]) <= int(str(datetime.date.today()).split('-')[0]):
                    return True
    return False


def name(name):
    if re.search(r'^[a-z,A-Z]+( [a-z,A-Z]+)?$', name) is not None and len(name) > 0:
        return True
    return False


def text(text):
    if re.search(r"[^(\w,., )]", text) is None and len(text) > 0:
        return True
    return False


def phone(phone):
    if re.search(r'^\d{7}$', phone) is not None:
        return True
    return False


def cellphone(cellphone):
    if re.search(r'^\d{10}$', cellphone) is not None:
        return True
    return False


def money(money):
    if re.search(r"^[0-9]+(\.[0-9]{1,2})?$", money) is None and len(money) != 0:
        return True
    return False
