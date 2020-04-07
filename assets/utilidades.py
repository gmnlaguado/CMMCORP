import re
import sqlite3
from datetime import date


class Costantes:
    panel = ["Plan de formación", "Plan implementación", "Ingrese el número\nde documento\ndel beneficiario",
             "Seleccione el número\nde documento\ndel beneficiario",
             "Esta acción requiere\nconexión a internet\n¿Desea continuar?",
             "El Beneficiario ya\ntiene registrada la\ncaracterización básica",
             "Formato de documento\nde identidad incorrecto.\nIngrese nuevamente",
             "Beneficiario existe en\notro proyecto, ¿Desea\ncopiar su C. Básica?"]

    infoGeneral = ["Información General", "Depto. Expedición", "Ciudad Expedición", "Dirección", "Rótulo",
                   "Teléfono Fijo", "Género", "Número Celular", "Agregar Número", "Cond. Discapacidad",
                   "Correo Electrónico", "Compruebe que los\ndatos estén correctos\nantes de continuar"]

    ideaNegocio = ["¿Es agropecuario?", "¿Necesita Colaboradores", "Por qué no había empezado", "¿Cómo surge la idea",
                   "¿Tiene Experiencia?", "Inversión Activos", "% Inversión Inicial", "Inversión Inicial",
                   "Ventas primer año"]

    unidadNegocio = ["Correo Electrónico", "Página Web", "Reg. Cámara de Comercio", "Rótulo", "Número Celular",
                     "Agregar Número", "Dirección", "Descripción", "Creación", "Descripción Pasivos",
                     "Teléfono Fijo"]



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



    sector = ["Sector Industrial", "Sector de Servicios", "Sector de Comercio", "Sector Agropecuario",
              "Sector de Transporte", "Sector Financiero", "Sector de la Construcción", "Sector Minero y Energético",
              "Sector Solidario", "Sector de Comunicaciones"]
    comoSurge = ["Oportunidad", "Necesidad"]
    cuantoTiempo = ["Completo", "Medio Tiempo", "Fin de Semana", "Horas"]
    estudiosAprendizaje = ["Si", "No"]
    experiencia = ["Si", "No"]
    productoServicio = ["Producto", "Servicio"]
    esAgropecuario = ["Si", "No"]
    necesitaColaboradores = ["Si", "No"]
    cuantosMeses = [str(numb) for numb in range(0, 40)]
    cuantoTiempo = ["De 1 a 4 Horas", "De 5 a 8 Horas", "Más de 8 Horas"]
    porqueNoEmpezaba = ["Falta de Tiempo", "Falta de recursos económicos", "Falta de motivación",
                        "Falta de conocimiento", "Otros"]
    procentajeInversion = ["< 50%", "50% - 100%", "0%"]





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

    @staticmethod
    def name(name):
        if re.search(r'[^(a-z,A-Z,\s)]', name) is None and len(name) != 0:
            return True
        return False

    @staticmethod
    def data(data):
        if re.search(r'^\d{2}[/]\d{2}[/]\d{4}$', data) is not None:
            data = data.split('/')
            if 0 <= int(data[0]) <= 31:
                if 0 <= int(data[1]) <= 12:
                    if 1900 <= int(data[2]) <= int(str(date.today()).split('-')[0]):
                        return True
        return False

    @staticmethod
    def fijo(fijo):
        if re.search(r'^\d{7}$', fijo) is not None:
            return True
        return False

    @staticmethod
    def celular(celular):
        if re.search(r'^\d{10}$', celular) is not None:
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


class InfoGeneral:
    @staticmethod
    def edad(fecha):
        hoy = [int(entero) for entero in str(date.today()).split('-')[::-1]]
        fecha = [int(entero) for entero in fecha.split('/')]
        anos = hoy[-1] - fecha[-1]
        if hoy[-2] == fecha[-2]:
            if hoy[-3] < fecha[-3]:
                anos -= 1
        elif hoy[-2] > fecha[-2]:
            anos -= 1

        if 15 <= anos <= 19:
            rango = '15-19'
        elif 20 <= anos <= 29:
            rango = '20-29'
        elif 30 <= anos <= 39:
            rango = '30-39'
        elif 40 <= anos <= 49:
            rango = '40-49'
        elif 50 <= anos <= 59:
            rango = '50-59'
        else:
            rango = '60 en adelante'
        return [anos, rango]

    @staticmethod
    def cargarDatos():
        retornar = [Costantes.tipoDocumento, Costantes.sexo, Costantes.tipoBeneficiario, Costantes.entorno,
                    Costantes.rotulo, Costantes.indicador, Costantes.genero, Costantes.etnia, Costantes.discapacidad]

        conn = sqlite3.connect('assets/dbs/base.db')
        c = conn.cursor()

        c.execute("SELECT nombre FROM paises")
        result = c.fetchall()
        result = [str(res[0]) for res in result]
        retornar.append(result)

        return retornar

    @staticmethod
    def comprobarTodo(dictionary):
        for key, value in dictionary.items():
            if key == "nombre":
                if not Comprobaciones.name(value.text):
                    return False
            if key == "apellido":
                if not Comprobaciones.name(value.text):
                    return False
            if key == "nacimiento":
                if not Comprobaciones.data(value.text):
                    return False
            if key == "tipoDocumento":
                if value.text == "Tipo de documento":
                    return False
            if key == "deptoExpedicion":
                if value.text == "Depto. Expedición":
                    return False
            if key == "ciudadExpedicion":
                if value.text == "Ciudad Expedición":
                    return False
            if key == "sexo":
                if value.text == "Sexo":
                    return False
            if key == "tipo":
                if value.text == "Tipo de Beneficiario":
                    return False
            if key == "nacionalidad":
                if value.text == "Nacionalidad":
                    return False
            if key == "pais":
                if value.text == "Pais de residencia":
                    return False
            if key == "departamentos":
                if value.text == "Departamento":
                    return False
            if key == "ciudades":
                if value.text == "Ciudad":
                    return False
            if key == "entorno":
                if value.text == "Entorno":
                    return False
            if key == "rotulo":
                if value.text == "Rótulo":
                    return False
            if key == "direccion":
                if value.text == "":
                    return False
            if key == "barrios":
                if value.text == "Barrio":
                    return False
            if key == "indicador":
                if value.text == "Indicador":
                    return False
            if key == "genero":
                if value.text == "Género":
                    return False
            if key == "celular":
                if not Comprobaciones.celular(value.text):
                    return False
            if key == "etnia":
                if value.text == "Etnia":
                    return False
            if key == "discapacidad":
                if value.text == "Cond. Discapacidad":
                    return False
        return True


class DiagnosticoPerfilP:
    @staticmethod
    def comprobarTodo(container_grid):
        for grid in container_grid.children:
            if len(grid.children) > 0:
                if not True in [box.active for box in grid.children]:
                    return False
        return True


class IdeaNegocio:
    @staticmethod
    def cargarDatos():
        retornar = [Costantes.sector, Costantes.comoSurge, Costantes.cuantoTiempo, Costantes.estudiosAprendizaje,
                    Costantes.experiencia, Costantes.productoServicio, Costantes.esAgropecuario,
                    Costantes.necesitaColaboradores, Costantes.cuantosMeses, Costantes.cuantoTiempo,
                    Costantes.porqueNoEmpezaba, Costantes.procentajeInversion]
        return retornar
