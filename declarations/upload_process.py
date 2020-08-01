# coding=utf-8
from declarations import class_declaration, querys


def uploadInformation():
    tablas = querys.lista_de_tablas()

    for tab in tablas:
        res = querys.obtener_toda_info(tab)
        if len(res) > 0:
            print(tab, res)

    for tabs in tablas:
        querys.limpiar_tabla(tabs)
