# coding=utf-8
from datetime import date


def chekingCompletes(children_list):
    for idx, child in enumerate(children_list):
        print(idx, child)
        if 'class_type' in dir(child):
            if child.class_type in ['spinner', 'input']:
                if not child.complete:
                    return False
            elif child.class_type == "container":
                for chil in child.children:
                    children_list.append(chil)
    return True


def ageCalculation(age):
    today = [int(integer) for integer in str(date.today()).split('-')[::-1]]
    data = [int(integer) for integer in age.split('/')]
    years = today[-1] - data[-1]
    if today[-2] == data[-2]:
        if today[-3] < data[-3]:
            years -= 1
    elif today[-2] < data[-2]:
        years -= 1
    return years


def rangeCalculation(age):
    if 15 <= age <= 19:
        return 1
    elif 20 <= age <= 29:
        return 2
    elif 30 <= age <= 39:
        return 3
    elif 40 <= age <= 49:
        return 4
    elif 50 <= age <= 59:
        return 5
    else:
        return 6


def formattingDate(datetime_date):
    datetime_date = '-'.join(datetime_date.split('/')[::-1])
    return datetime_date
