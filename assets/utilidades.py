import re
import sqlite3


class Costantes:
    panel = ["Plan de formación", "Plan implementación", "Ingrese el número\nde documento\ndel beneficiario",
             "Seleccione el número\nde documento\ndel beneficiario",
             "Esta acción requiere\nconexión a internet\n¿Desea continuar?",
             "El Beneficiario ya\ntiene registrada la\ncaracterización básica",
             "Formato de documento\nde identidad incorrecto.\nIngrese nuevamente",
             "Beneficiario existe en\notro proyecto, ¿Desea\ncopiar su C. Básica?"]

    infoGeneral = ["Información General", "Departamento Expedición", "Ciudad Expedición", "Dirección", "Rótulo",
                   "Teléfono Fijo", "Género", "Número Celular", "Agregar Número", "Condición Discapacidad",
                   "Correo Electrónico", "Compruebe que los\ndatos estén correctos\nantes de continuar"]

    ideaNegocio = ["¿Es agropecuario?", "¿Necesita Colaboradores", "Por qué no había empezado", "¿Cómo surge la idea",
                   "¿Tiene Experiencia?", "Inversión Activos", "% Inversión Inicial", "Inversión Inicial",
                   "Ventas primer año"]

    unidadNegocio = ["Correo Electrónico", "Página Web", "Reg. Cámara de Comercio", "Rótulo", "Número Celular",
                     "Agregar Número", "Dirección", "Descripción", "Creación", "Descripción Pasivos",
                     "Teléfono Fijo"]


class Comprobaciones:
    @staticmethod
    def username(username):
        if re.search(r'^\w+$', username) is not None:
            return True
        return False

    @staticmethod
    def password(password):
        if re.search(r'[^(\w,-,.)]', password) is None and len(password) > 0:
            return True
        return False


class Login:
    @staticmethod
    def checkData(username, password):
        if username and password:
            return True
        return False

    @staticmethod
    def checkIfRight(username, password):
        conn = sqlite3.connect('assets/dbs/base.db')
        c = conn.cursor()
        c.execute("SELECT password FROM operarios WHERE username = :username", {'username': username})
        result = c.fetchone()
        if result is None:
            return "Usuario no existe"
        else:
            if password == result[0]:
                return ""
        return "Contraseña Incorrecta"

    @staticmethod
    def proyectos(username):
        conn = sqlite3.connect('assets/dbs/base.db')
        c = conn.cursor()
        c.execute("SELECT nombre FROM proyectos INNER JOIN operariosProyectos ON operariosProyectos.fkProyecto = "
                  "proyectos.idProyecto WHERE operariosProyectos.fkOperario = :username", {'username': username})
        result = c.fetchall()
        result = [res[0] for res in result]
        return result


class Panel:
    @staticmethod
    def buscarBeneficiario(beneficiario, string):
        if beneficiario != "":
            string = string.split(" ")
            proyecto = string[3]
            operario = string[1]
            conn = sqlite3.connect('assets/dbs/base.db')
            c = conn.cursor()
            c.execute("SELECT fkBeneficiario FROM beneficiariosProyectos WHERE fkProyecto = (SELECT idProyecto FROM "
                      "proyectos WHERE nombre = :proyecto)", {'proyecto': proyecto})
            result = c.fetchall()
            result = [str(res[0]) for res in result]
            if beneficiario in result:
                return "no"
            else:
                c.execute("SELECT fkBeneficiario, nombre FROM beneficiariosProyectos INNER JOIN proyectos ON "
                          "proyectos.idProyecto = beneficiariosProyectos.fkProyecto WHERE fkProyecto IN (SELECT "
                          "fkProyecto FROM operariosProyectos WHERE fkOperario =:operario)", {'operario': operario})
                result = c.fetchall()
                pros = []
                for ben, pro in result:
                    if beneficiario == str(ben):
                        pros.append(pro)
                if len(pros) > 0:
                    return pros
                else:
                    return "continua"
        return [""]

    @staticmethod
    def tipoBeneficiario(beneficiario):
        conn = sqlite3.connect('assets/dbs/base.db')
        c = conn.cursor()
        c.execute("SELECT tipo FROM beneficiarios WHERE documento = :beneficiario", {'beneficiario': beneficiario})
        result = c.fetchone()
        if result is not None:
            return result[0]
