# coding=utf-8
import sqlite3


class MyDB(object):
    def __init__(self, database):
        self._db_connection = sqlite3.connect(f'databases/{database}/{database}.db')
        self._db_cur = self._db_connection.cursor()

    def query(self, query, params):
        return self._db_cur.execute(query, params)

    def parametricQuery(self, query):
        return self._db_cur.execute(query)

    def commit(self, query, params):
        self._db_cur.execute(query, params)
        return self._db_connection.commit()

    def __del__(self):
        self._db_connection.close()


def idOperator(username):
    db = MyDB('register')
    result = db.query("SELECT document FROM odp_operario WHERE username = :username", {'username': username}).fetchone()
    if result is not None:
        return result[0]


def idProject(project):
    db = MyDB('register')
    result = db.query("SELECT id FROM proyectos WHERE name = :project", {'project': project}).fetchone()
    if result is not None:
        return result[0]


def payeeProjects(project):
    db = MyDB('register')
    result = db.query("SELECT payeeDocument FROM beneficiario_proyectos WHERE project = :project",
                      {'project': project}).fetchall()
    if result is not None:
        return [res[0] for res in result]


def passwordOperator(document):
    db = MyDB('register')
    result = db.query("SELECT password FROM odp_operario WHERE document = :document", {'document': document}).fetchone()
    if result is not None:
        return result[0]


def projectsOperator(document):
    db = MyDB('register')
    result = db.query("SELECT fkProject FROM odp_operario_proyectos WHERE fkOperator = :document",
                      {'document': document}).fetchall()
    if result is not None:
        return [res[0] for res in result]


def nameProject(project):
    db = MyDB('register')
    result = db.query("SELECT name FROM proyectos WHERE id = :project", {'project': project}).fetchone()
    if result is not None:
        return result[0]


def indicator(department):
    db = MyDB('parametric')
    result = db.query("SELECT indicative FROM departments WHERE id = :department",
                      {'department': department}).fetchone()
    if result is not None:
        return result[0]


def parametricList(tabl):
    db = MyDB('parametric')
    result = db.parametricQuery("SELECT data FROM %s" % tabl).fetchall()
    if result is not None:
        return [res[0] for res in result]


def idParametrics(table, data):
    db = MyDB('parametric')
    result = db.parametricQuery("SELECT id FROM %s WHERE data = '%s'" % (table, data)).fetchone()
    if result is not None:
        return result[0]


def dataParametrics(table, ids):
    db = MyDB('parametric')
    result = db.parametricQuery("SELECT data FROM %s WHERE id = '%s'" % (table, ids)).fetchone()
    if result is not None:
        return result[0]


def bringDepartments(country):
    db = MyDB('parametric')
    result = db.query("SELECT data FROM departments WHERE fkCountry = :country", {'country': country}).fetchall()
    if result is not None:
        return [res[0] for res in result]


def idDepartments(department):
    db = MyDB('parametric')
    result = db.query("SELECT id FROM departments WHERE data = :department", {'department': department}).fetchone()
    if result is not None:
        return result[0]


def bringCities(department):
    db = MyDB('parametric')
    result = db.query("SELECT data FROM cities WHERE fkDepartment = :department", {'department': department}).fetchall()
    if result is not None:
        return [res[0] for res in result]


def idCities(city):
    db = MyDB('parametric')
    result = db.query("SELECT id FROM cities WHERE data = :city", {'city': city}).fetchone()
    if result is not None:
        return result[0]


def bringNeighborhoods(city):
    db = MyDB('parametric')
    result = db.query("SELECT data FROM neighborhoods WHERE fkCities = :city", {'city': city}).fetchall()
    if result is not None:
        return [res[0] for res in result]


def loadPayee(info):
    db = MyDB('register')
    db.commit("INSERT INTO informacion_general_beneficiario VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", info)


def loadPayeeProjects(info):
    db = MyDB('register')
    db.commit("INSERT INTO beneficiario_proyectos VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)", info)


def loadProductionProfileDiag(info):
    db = MyDB('register')
    db.commit("INSERT INTO diagnostico_de_perfil_productivo VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?"
              ",?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", info)


def loadBussinesIdea(info):
    db = MyDB('register')
    db.commit("INSERT INTO idea_de_negocio VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", info)


def loadBussinesUnit(info):
    db = MyDB('register')
    db.commit("INSERT INTO unidad_de_negocio VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", info)


def bringColumns(table):
    db = MyDB('register')
    result = db.parametricQuery("PRAGMA table_info(%s)" % table).fetchall()
    if result is not None:
        return [res[1] for res in result]


def bringData(table):
    db = MyDB('register')
    result = db.parametricQuery("SELECT * FROM %s" % table).fetchall()
    return result

def bringProgramFromEducationPlan():
    db = MyDB('parametric')
    result = db.parametricQuery("SELECT program FROM educationPlan GROUP BY program").fetchall()
    if result is not None:
        return [res[0] for res in result]

def bringLineFromEducationPlan(program):
    db = MyDB('parametric')
    result = db.parametricQuery("SELECT line FROM educationPlan WHERE program = '%s' GROUP BY line" % program).fetchall()
    if result is not None:
        return [res[0] for res in result]

def bringLevelFromEducationPlan(program, line):
    db = MyDB('parametric')
    result = db.parametricQuery("SELECT level FROM educationPlan WHERE program = '%s' AND line = '%s' GROUP BY level" % (program, line)).fetchall()
    if result is not None:
        return [res[0] for res in result]

def bringDescriptionsFromEducationPlan(program, line, level):
    db = MyDB('parametric')
    result = db.parametricQuery("SELECT description FROM educationPlan WHERE program = '%s' AND line = '%s' AND level = '%s'" % (program, line, level)).fetchall()
    if result is not None:
        return [res[0] for res in result]

def bringCIUU():
    db = MyDB('parametric')
    result = db.parametricQuery("SELECT id FROM ciiu").fetchall()
    if result is not None:
        return [str(res[0]) for res in result]


def cargar_caracterizacion_ampliada(info):
    db = MyDB('register')
    db.commit("INSERT INTO caracterizacion_ampliada VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", info)


def cargar_caracterizacion_ampliada_hijos(info):
    db = MyDB('register')
    db.commit("INSERT INTO caracterizacion_ampliada_informacion_hijos VALUES (?,?,?,?,?,?,?,?)", info)


def cargar_caracterizacion_ampliada_personas(info):
    db = MyDB('register')
    db.commit("INSERT INTO caracterizacion_ampliada_informacion_personas_a_cargo VALUES (?,?,?,?,?,?,?,?)", info)


def lista_de_caracterizaciones(project):
    db = MyDB('register')
    result = db.query("SELECT fkPayee FROM caracterizacion_ampliada WHERE fkProject = :project", {'project': project}).fetchall()
    if result is not None:
        return [res[0] for res in result]


def cargar_monitoreo(info):
    db = MyDB('register')
    db.commit("INSERT INTO monitoreo VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", info)


def cargar_diagnostico_empresarial(info):
    db = MyDB('register')
    db.commit("INSERT INTO diagnostico_empresarial VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", info)


def tipo_de_beneficiario(beneficiario):
    db = MyDB('register')
    result = db.query("SELECT payeeType FROM informacion_general_beneficiario WHERE document = :beneficiario",
                      {'beneficiario': beneficiario}).fetchone()
    if result is not None:
        return result[0]


def numero_de_monitoreo(beneficiario):
    db = MyDB('register')
    result = db.query("SELECT numero_monitoreo FROM monitoreo WHERE fk_beneficiario = :beneficiario",
                      {'beneficiario': beneficiario}).fetchall()
    if result is not None:
        return max([res[0] for res in result])


def plan_de_formacion_habilitado(beneficiario):
    db = MyDB('register')
    result = db.query("SELECT plan_de_formacion FROM beneficiario_proyectos WHERE payeeDocument = :beneficiario",
                      {'beneficiario': beneficiario}).fetchone()
    if result is not None:
        return result[0]


def plan_de_implementacion_habilitado(beneficiario):
    db = MyDB('register')
    result = db.query("SELECT plan_de_implementacion FROM beneficiario_proyectos WHERE payeeDocument = :beneficiario",
                      {'beneficiario': beneficiario}).fetchone()
    if result is not None:
        return result[0]


def habilitar_plan_de_formacion(beneficiario, project):
    db = MyDB('register')
    db.commit("UPDATE beneficiario_proyectos SET plan_de_formacion = 1 WHERE payeeDocument = :beneficiario AND project = :project", (beneficiario, project))


def habilitar_plan_de_implementacion(beneficiario, project):
    db = MyDB('register')
    db.commit("UPDATE beneficiario_proyectos SET plan_de_implementacion = 1 WHERE payeeDocument = :beneficiario AND project = :project", (beneficiario, project))


def deshabilitar_plan_de_formacion(beneficiario, project):
    db = MyDB('register')
    db.commit("UPDATE beneficiario_proyectos SET plan_de_formacion = 2 WHERE payeeDocument = :beneficiario AND project = :project", (beneficiario, project))


def obtener_estado(beneficiario):
    db = MyDB('register')
    result = db.query("SELECT status FROM beneficiario_proyectos WHERE payeeDocument = :beneficiario",
                      {'beneficiario': beneficiario}).fetchone()
    if result is not None:
        return result[0]


def inactivar_beneficiario(beneficiario, project):
    db = MyDB('register')
    db.commit("UPDATE beneficiario_proyectos SET status = 2 WHERE payeeDocument = :beneficiario AND project = :project",
        (beneficiario, project))


def traer_id_de_actividad_de_formacion(actividad):
    db = MyDB('parametric')
    result = db.query("SELECT id FROM educationPlan WHERE description = :actividad",
                      {'actividad': actividad}).fetchone()
    if result is not None:
        return result[0]


def cargar_plan_de_formacion(info):
    db = MyDB('register')
    db.commit("INSERT INTO plan_de_formacion VALUES (?,?,?,?,?,?,?,?,?)", info)


def traer_actividades_formacion(beneficiario, proyecto):
    db = MyDB('register')
    result = db.query("SELECT id_actividad, fecha_actividad, completada FROM plan_de_formacion WHERE beneficiario = :beneficiario AND proyecto = :proyecto",{'beneficiario': beneficiario, 'proyecto': proyecto}).fetchall()
    if result is not None:
        return [list(res) for res in result]


def traer_descripcion_actividad_formacion(id_actividad):
    db = MyDB('parametric')
    result = db.query("SELECT description FROM educationPlan WHERE id = :id_actividad",
                      {'id_actividad': id_actividad}).fetchone()
    if result is not None:
        return result[0]


def dar_actividad_de_formacion_como_finalizada(beneficiario, project, actividad, fecha):
    db = MyDB('register')
    db.commit("UPDATE plan_de_formacion SET completada = 1, fecha_realizada = :fecha WHERE beneficiario = :beneficiario AND proyecto = :project AND id_actividad = :actividad",
              (fecha, beneficiario, project, actividad))


def dar_terminada_formacion(beneficiario, project):
    db = MyDB('register')
    db.commit("UPDATE beneficiario_proyectos SET concluido_formacion = 1 WHERE payeeDocument = :beneficiario AND project = :project",(beneficiario, project))


def comprobar_plan_de_formacion(beneficiario, project):
    db = MyDB('register')
    result = db.query("SELECT concluido_formacion FROM beneficiario_proyectos WHERE payeeDocument = :beneficiario AND project = :project",
                      {'beneficiario': beneficiario, 'project': project}).fetchone()
    if result is not None:
        return result[0]


def traer_puntajes_diagnostico(beneficiario, project):
    db = MyDB('register')
    result = db.query("SELECT categoria_1, categoria_2, categoria_3, categoria_4, categoria_5, categoria_6, categoria_7, categoria_8, categoria_9  FROM diagnostico_empresarial WHERE fk_beneficiario = :beneficiario AND fk_proyecto = :project",
        {'beneficiario': beneficiario, 'project': project}).fetchone()
    return list(result)


def modificar_etapa_del_proceso(beneficiario, project, etapa):
    db = MyDB('register')
    db.commit("UPDATE beneficiario_proyectos SET etapa_del_proceso = :etapa WHERE payeeDocument = :beneficiario AND project = :project",
        (etapa, beneficiario, project))

