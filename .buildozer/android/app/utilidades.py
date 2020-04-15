# coding=utf-8
import re
import sqlite3


class Comprobaciones:
    @staticmethod
    def username(username):
        if re.search(r'^\w+$', username) is not None:
            return True
        return False

    @staticmethod
    def password(password):
        if re.search(r'[^(\w,.)]', password) is None and len(password) > 0:
            return True
        return False


class MyDB(object):
    def __init__(self):
        self._db_connection = sqlite3.connect('datos.db')
        self._db_cur = self._db_connection.cursor()

    def query(self, query, params):
        return self._db_cur.execute(query, params)

    def __del__(self):
        self._db_connection.close()


class Login:
    @staticmethod
    def checkIfRight(usuario, contrasena):
        db = MyDB()
        resultado = db.query("SELECT password FROM operarios WHERE username = :username",
                             {'username': usuario}).fetchone()
        if resultado is None:
            return "Usuario no existe"
        elif contrasena == resultado[0]:
            return ""
        return "Contraseña Incorrecta"

    @staticmethod
    def proyectos(username: object) -> object:
        db = MyDB()
        resultado = db.query("SELECT nombre FROM proyectos INNER JOIN operariosProyectos ON "
                             "operariosProyectos.fkProyecto = proyectos.idProyecto WHERE "
                             "operariosProyectos.fkOperario = :username", {'username': username}).fetchall()
        resultado = [res[0] for res in resultado]
        return resultado


class Panel:
    @staticmethod
    def buscarBeneficiario(beneficiario, string):
        if beneficiario != "":
            string = string.split(" ")
            proyecto = string[3]
            operario = string[1]
            db = MyDB()
            resultado = db.query("SELECT fkBeneficiario FROM beneficiariosProyectos WHERE fkProyecto = (SELECT "
                                 "idProyecto FROM proyectos WHERE nombre = :proyecto)",
                                 {'proyecto': proyecto}).fetchall()
            resultado = [res[0] for res in resultado]
            if beneficiario in resultado:
                return "Ya tiene C. Básica"
            else:
                resultado = db.query("SELECT fkBeneficiario, nombre FROM beneficiariosProyectos INNER JOIN proyectos "
                                     "ON proyectos.idProyecto = beneficiariosProyectos.fkProyecto WHERE fkProyecto IN "
                                     "(SELECT fkProyecto FROM operariosProyectos WHERE fkOperario =:operario)",
                                     {'operario': operario}).fetchall()
                pros = []
                for ben, pro in resultado:
                    if beneficiario == ben:
                        pros.append(pro)
                if len(pros) > 0:
                    return ' '.join(pros)
                else:
                    return "No existe"
