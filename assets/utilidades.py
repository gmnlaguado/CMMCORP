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

    ideaNegocio = ["¿Es agropecuario?", "Necesita Colaboradores", "Por qué no había empezado", "Cómo surge la idea",
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
    cuantosMeses = [str(numb) for numb in range(0, 50)]
    cuantoTiempo = ["De 1 a 4 Horas", "De 5 a 8 Horas", "Más de 8 Horas"]
    porqueNoEmpezaba = ["Falta de Tiempo", "Falta de recursos económicos", "Falta de motivación",
                        "Falta de conocimiento", "Otros"]
    procentajeInversion = ["< 50%", "50% - 100%", "0%"]

    cuantosSocios = [str(numb) for numb in range(0, 50)]
    regCamara = ["Si", "No"]
    conContrato = [str(numb) for numb in range(0, 50)]
    sinContrato = [str(numb) for numb in range(0, 50)]


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

    @staticmethod
    def dinero(dinero):
        if re.search(r"[^(0-9,.)]", dinero) is None and len(dinero) != 0:
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

        conn = sqlite3.connect('assets/dbs/base.db')
        c = conn.cursor()

        c.execute("SELECT idCIIU FROM cIIU")
        result = c.fetchall()
        result = [str(res[0]) for res in result]
        retornar.append(result)

        c.execute("SELECT sector FROM cIIU")
        result = c.fetchall()
        result = [str(res[0]) for res in result]
        retornar.append(result)

        return retornar

    @staticmethod
    def comprobarTodo(dictionary):
        for key, value in dictionary.items():
            if key == "sectorEmpresarial":
                if value.text == "Sector Empresarial":
                    return False
            if key == "ciudades":
                if value.text == "Ciudad":
                    return False
            if key == "estudios":
                if value.text == "Estudios sobre el tema":
                    return False
            if key == "esAgropecuario":
                if value.text == "¿Es agropecuario?":
                    return False
            if key == "necesitaColaboradores":
                if value.text == "Necesita Colaboradores":
                    return False
            if key == "tiempoSemanal":
                if value.text == "Tiempo semanal a dedicar":
                    return False
            if key == "porqueNo":
                if value.text == "Por qué no había empezado":
                    return False
            if key == "mesesQueLleva":
                if value.text == "Meses que lleva el negocio":
                    return False
            if key == "ciiu":
                if value.text == "CIIU":
                    return False
            if key == "comoSurge":
                if value.text == "Cómo surge la idea":
                    return False
            if key == "tieneExperiencia":
                if value.text == "¿Tiene Experiencia?":
                    return False
            if key == "departamentos":
                if value.text == "Departamento":
                    return False
            if key == "tiempoADedicar":
                if value.text == "Tiempo a dedicar":
                    return False
            if key == "productoServicio":
                if value.text == "Producto / Servicio":
                    return False
            if key == "porcentajeInversion":
                if value.text == "% Inversión Inicial":
                    return False
            if key == "inversionActivos":
                if not Comprobaciones.dinero(value.text):
                    return False
            if key == "ventasPrimerMes":
                if not Comprobaciones.dinero(value.text):
                    return False
            if key == "inversionInicial":
                if not Comprobaciones.dinero(value.text):
                    return False
            if key == "invCapitalTrabajo":
                if not Comprobaciones.dinero(value.text):
                    return False
            if key == "ventasPrimerAno":
                if not Comprobaciones.dinero(value.text):
                    return False
            if key == "imagine":
                if not Comprobaciones.name(value.text):
                    return False
            if key == "listaProductos":
                if not Comprobaciones.name(value.text):
                    return False
            if key == "listaColaboradores":
                if not Comprobaciones.name(value.text):
                    return False
        return True


class UnidadNegocio:
    @staticmethod
    def cargarDatos():
        retornar = [Costantes.cuantosSocios, Costantes.rotulo, Costantes.indicador, Costantes.sector,
                    Costantes.regCamara, Costantes.conContrato, Costantes.sinContrato]

        conn = sqlite3.connect('assets/dbs/base.db')
        c = conn.cursor()

        c.execute("SELECT idCIIU FROM cIIU")
        result = c.fetchall()
        result = [str(res[0]) for res in result]
        retornar.append(result)

        c.execute("SELECT sector FROM cIIU")
        result = c.fetchall()
        result = [str(res[0]) for res in result]
        retornar.append(result)

        pais = "colombia"
        c.execute("SELECT departamentos.nombre FROM departamentos INNER JOIN paises ON paises.idPais = "
                  "departamentos.fkPais WHERE paises.nombre = :pais", {'pais': pais})
        deptos = [li[0] for li in c.fetchall()]

        retornar.append(deptos)

        return retornar

    @staticmethod
    def comprobarTodo(dictionary):
        for key, value in dictionary.items():
            if key == "unidad":
                if not Comprobaciones.name(value.text):
                    return False
            if key == "existe":
                if value.text == "Si existe, seleccione":
                    return False
            if key == "cuantosSocios":
                if value.text == "Cantidad de socios":
                    return False
            if key == "ciiu":
                if value.text == "CIIU":
                    return False
            if key == "sector":
                if value.text == "Sector Empresarial":
                    return False
            if key == "regCamara":
                if value.text == "Reg. Cámara de Comercio":
                    return False
            if key == "conContrato":
                if value.text == "Colaborador con contrato":
                    return False
            if key == "sinContrato":
                if value.text == "Colaborador sin contrato":
                    return False
            if key == "departamentos":
                if value.text == "Departamento":
                    return False
            if key == "ciudades":
                if value.text == "Ciudad":
                    return False
            if key == "direccion":
                if value.text == "":
                    return False
            if key == "telFijo":
                if not Comprobaciones.fijo(value.text):
                    return False
            if key == "rotulo":
                if value.text == "Rótulo":
                    return False
            if key == "indicador":
                if value.text == "Indicador":
                    return False
            if key == "celular":
                if value.text == "celular":
                    return False
            if key == "descripcion":
                if not Comprobaciones.name(value.text):
                    return False
            if key == "portafolio":
                if not Comprobaciones.name(value.text):
                    return False
            if key == "creacion":
                if not Comprobaciones.data(value.text):
                    return False
            if key == "nit":
                if not Comprobaciones.dinero(value.text):
                    return False
            if key == "descripcionPasivos":
                if not Comprobaciones.name(value.text):
                    return False
            if key == "celular":
                if not Comprobaciones.celular(value.text):
                    return False
        return True


class CBasica:
    @staticmethod
    def organizar(panel, info, diag, idea, unidad):
        proyecto = panel.proyecto.text.split(" ")[-1]
        beneficiariosProyectos = [proyecto, panel.beneficiario.text]
        beneficiarios = [panel.beneficiario.text, info.nombre.text, info.apellido.text, info.nacimiento.text,
                         info.nacionalidad.text, info.tipoDocumento.text, info.ciudadExpedicion.text, info.pais.text,
                         info.departamentos.text, info.ciudades.text, info.barrios.text, info.entorno.text,
                         info.direccion.text, info.sexo.text, info.indicador.text, info.fijo.text, info.email.text,
                         info.genero.text, info.etnia.text, info.discapacidad.text, info.tipo.text]

        conn = sqlite3.connect('assets/dbs/base.db')
        c = conn.cursor()

        c.execute("SELECT idPais FROM paises WHERE nombre = :nombre", {'nombre': info.nacionalidad.text})
        result = c.fetchone()
        beneficiarios[4] = result[0]

        c.execute("SELECT idCiudad FROM ciudades WHERE nombre = :nombre", {'nombre': info.ciudadExpedicion.text})
        result = c.fetchone()
        beneficiarios[6] = result[0]

        c.execute("SELECT idPais FROM paises WHERE nombre = :nombre", {'nombre': info.pais.text})
        result = c.fetchone()
        beneficiarios[7] = result[0]

        c.execute("SELECT idDepartamento FROM departamentos WHERE nombre = :nombre", {'nombre': info.departamentos.text})
        result = c.fetchone()
        beneficiarios[8] = result[0]

        c.execute("SELECT idCiudad FROM ciudades WHERE nombre = :nombre", {'nombre': info.ciudades.text})
        result = c.fetchone()
        beneficiarios[9] = result[0]

        c.execute("SELECT idBarrio FROM barrios WHERE nombre = :nombre", {'nombre': info.barrios.text})
        result = c.fetchone()
        beneficiarios[10] = result[0]


        print(beneficiariosProyectos)
        print("\n\n\n")
        print(beneficiarios)
        print("\n\n\n")

        diagnosticoPerfilProductivo = []
        count = 0
        for grid in diag.children:
            if len(grid.children) > 0:
                repp = [box.active for box in grid.children][::-1].index(True)
                diagnosticoPerfilProductivo.append([panel.beneficiario.text, 70 - count, repp])
                count += 1

        print(diagnosticoPerfilProductivo[::-1])
        print("\n\n\n")

        if info.tipo.text == "Microempresario":
            unidadNegocio = [proyecto, panel.beneficiario.text, unidad.unidad.text,
                             unidad.departamentos.text, unidad.ciudades.text, unidad.cuantosSocios.text,
                             unidad.direccion.text, unidad.ciiu.text, unidad.indicador.text, unidad.telFijo.text,
                             unidad.email.text, unidad.paginaWeb.text, unidad.descripcion.text, unidad.portafolio.text,
                             unidad.creacion.text, unidad.nit.text, unidad.descripcionPasivos.text,
                             unidad.regCamara.text, unidad.conContrato.text, unidad.sinContrato.text]

            c.execute("SELECT idDepartamento FROM departamentos WHERE nombre = :nombre",
                      {'nombre': unidad.departamentos.text})
            result = c.fetchone()
            unidadNegocio[3] = result[0]

            c.execute("SELECT idCiudad FROM ciudades WHERE nombre = :nombre", {'nombre': unidad.ciudades.text})
            result = c.fetchone()
            unidadNegocio[4] = result[0]


            print(unidadNegocio)
            print("\n\n\n")
            CBasica.limpieza(False, info, diag, unidad)
        else:
            ideaNegocio = [proyecto, panel.beneficiario.text, idea.emprendimiento.text, idea.sectorEmpresarial.text,
                           idea.ciiu.text, idea.departamentos.text, idea.ciudades.text, idea.comoSurge.text,
                           idea.tiempoADedicar.text, idea.estudios.text, idea.tieneExperiencia.text,
                           idea.productoServicio.text, idea.listaProductos.text, idea.esAgropecuario.text,
                           idea.portafolio.text, idea.inversionActivos.text, idea.inversionInicial.text,
                           idea.porcentajeInversion.text, idea.invCapitalTrabajo.text, idea.ventasPrimerMes.text,
                           idea.ventasPrimerAno.text, idea.necesitaColaboradores.text, idea.listaColaboradores.text,
                           idea.tiempoSemanal.text, idea.porqueNo.text, idea.mesesQueLleva.text, idea.imagine.text]

            c.execute("SELECT idDepartamento FROM departamentos WHERE nombre = :nombre",
                      {'nombre': idea.departamentos.text})
            result = c.fetchone()
            ideaNegocio[5] = result[0]

            c.execute("SELECT idCiudad FROM ciudades WHERE nombre = :nombre", {'nombre': idea.ciudades.text})
            result = c.fetchone()
            ideaNegocio[6] = result[0]

            print(ideaNegocio)
            print("\n\n\n")
            CBasica.limpieza(True, info, diag, idea)

    @staticmethod
    def limpieza(limpiaridea, info, diag, ideaunidad):
        limpiezaInfoGeneral = ["", "", "", "Edad", "Rango", "Tipo de documento", Costantes.infoGeneral[1],
                               Costantes.infoGeneral[2], "Sexo", "Tipo de Beneficiario", "Nacionalidad",
                               "Pais de residencia", "Departamento", "Ciudad", "Entorno", Costantes.infoGeneral[4], "",
                               "Barrio", "Indicador", "", Costantes.infoGeneral[6], "", "", "Etnia",
                               Costantes.infoGeneral[9], "", ""]

        for idx, ids in enumerate(info.values()):
            ids.text = limpiezaInfoGeneral[idx]
            if limpiezaInfoGeneral[idx] != "":
                ids.background_color = 61/255, 119/255, 0/255, 0.7


        for grid in diag.children:
            if len(grid.children) > 0:
                for box in grid.children:
                    box.active = False

        if limpiaridea:
            limpiezaideanegocios = ["", "Sector Empresarial", "Ciudad", "Estudios sobre el tema",
                                    Costantes.ideaNegocio[0], Costantes.ideaNegocio[1], "Tiempo semanal a dedicar",
                                    Costantes.ideaNegocio[2], "Meses que lleva el negocio", "CIIU",
                                    Costantes.ideaNegocio[3], Costantes.ideaNegocio[4], "Departamento",
                                    "Tiempo a dedicar", "Producto / Servicio", "", "", Costantes.ideaNegocio[6], "",
                                    "", "", "", "", "", "", ""]

            for idx, ids in enumerate(ideaunidad.values()):
                ids.text = limpiezaideanegocios[idx]
                if limpiezaideanegocios[idx] != "":
                    ids.background_color = 61 / 255, 119 / 255, 0 / 255, 0.7

        else:
            limpiezaunidadnegocios = ["", "Si existe, seleccione", "Cantidad de socios", "CIIU", "", "",
                                      "Sector Empresarial", Costantes.unidadNegocio[2], "Colaborador con contrato",
                                      "Colaborador sin contrato", "Departamento", "Ciudad", "", "",
                                      Costantes.unidadNegocio[3], "Indicador", "", "", "", "", "", "", ""]

            for idx, ids in enumerate(ideaunidad.values()):
                ids.text = limpiezaunidadnegocios[idx]
                if limpiezaunidadnegocios[idx] != "":
                    ids.background_color = 61 / 255, 119 / 255, 0 / 255, 0.7
