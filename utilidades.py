# coding=utf-8
import re
import sqlite3


class Costantes:
    tipoDocumento = ["Cédula de Ciudadania", "Tarjeta de Identidad", "Cédula de Extranjería", "Pasaporte", "Otros"]
    sexo = ["Mujer", "Hombre", "Intersexual"]
    tipoBeneficiario = ["Emprendedor", "Microempresario"]
    entorno = ["Rural", "Urbano"]
    rotulo = ["Administración", "Apartamento", "Autopista", "Avenida", "Avenida Carrera", "Barrio", "Bloque", "Bodega",
              "Calle", "Carrera", "Carretera", "Casa", "Centro Comercial", "Consultorio", "Diagonal", "Finca", "Garaje",
              "Interior", "Kilometro", "Local", "Lote", "Manzana", "Mezzanine", "Norte", "Occidente", "Oficina",
              "Oriente", "Piso", "Salon Comunal", "Sur", "Torre", "Transversal", "Unidad", "Urbanización", "Variante",
              "Vereda", "Zona", "Zona Franca"]
    indicador = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    genero = ["Femenino", "Masculino", "Transgenero"]
    etnia = ["Afrodescendiente", "Raizal", "Palenquera", "Indígenas", "Rom", "Mestizo", "Otro", "No Aplica"]
    discapacidad = ["Física", "Cognitiva", "Sensorial", "Intelectual", "Psicosocial", "Múltiple", "Ninguna", "ND"]


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


class InfoGeneral:
    @staticmethod
    def cargarDatos():
        retornar = [Costantes.tipoDocumento, Costantes.sexo, Costantes.tipoBeneficiario, Costantes.entorno,
                    Costantes.rotulo, Costantes.indicador, Costantes.genero, Costantes.etnia, Costantes.discapacidad]
        db = MyDB()
        resultado = db.query("SELECT nombre FROM paises", {None: None}).fetchall()
        resultado = [str(res[0]) for res in resultado]
        retornar.append(resultado)

        resultado = db.query("SELECT departamentos.nombre FROM departamentos INNER JOIN paises ON paises.idPais = "
                  "departamentos.fkPais WHERE paises.nombre = 'colombia'", {None: None}).fetchall()
        resultado = [li[0] for li in resultado]
        retornar.append(resultado)
        return retornar

    @staticmethod
    def cargarDepartamentos(pais):
        db = MyDB()
        resultado = db.query("SELECT departamentos.nombre FROM departamentos INNER JOIN paises ON paises.idPais = "
                             "departamentos.fkPais WHERE paises.nombre = :pais", {'pais': pais}).fetchall()
        resultado = [li[0] for li in resultado]
        return resultado

    @staticmethod
    def cargarCiudades(departamento):
        db = MyDB()
        resultado = db.query("SELECT ciudades.nombre FROM ciudades INNER JOIN departamentos ON "
                             "departamentos.idDepartamento = ciudades.fkDepartamento WHERE departamentos.nombre = "
                             ":departamento", {'departamento': departamento}).fetchall()
        resultado = [li[0] for li in resultado]
        return resultado

    @staticmethod
    def cargarBarrios(ciudad):
        db = MyDB()
        resultado = db.query("SELECT barrios.nombre FROM barrios INNER JOIN ciudades ON ciudades.idCiudad = "
                  "barrios.fkCiudad WHERE ciudades.nombre = :ciudad", {'ciudad': ciudad}).fetchall()
        resultado = [li[0].lower() for li in resultado]
        return resultado

