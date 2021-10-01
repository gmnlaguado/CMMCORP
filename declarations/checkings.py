# coding=utf-8
import re
from datetime import datetime


def username(username):
    if re.search(r"^[a-zA-Z0-9]+$", username) is not None and len(username) > 0:
        return True
    return False


def password(password):
    if re.search(r"[^\w,.]", password) is None and len(password) > 0:
        return True
    return False


def date(date):
    format = "%d/%m/%Y"
    try:
        datetime.strptime(date, format)
        return True

    except ValueError:
        return False


def after_date(date):
    format = "%d/%m/%Y"
    try:
        date_formater = datetime.strptime(date, format)
        if date_formater > datetime.now():
            return True
        return False

    except ValueError:
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
    if re.search(r"^[0-9]{0,3}(\.[0-9]{3}){0,3}$", money) is not None and len(money) > 3:
        return True
    return False

def nit(nit):
    if re.search(r"^[0-9]{8,10}(\-[0-9]{1}){1}$", nit) is not None and len(nit) != 0:
        return True
    return False
