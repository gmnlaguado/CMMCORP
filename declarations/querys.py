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
    result = db.query("SELECT document FROM operator WHERE username = :username", {'username': username}).fetchone()
    if result is not None:
        return result[0]


def idProject(project):
    db = MyDB('register')
    result = db.query("SELECT id FROM projects WHERE name = :project", {'project': project}).fetchone()
    if result is not None:
        return result[0]


def payeeProjects(project):
    db = MyDB('register')
    result = db.query("SELECT fkPayee FROM payeeProjects WHERE fkProject = :project",
                      {'project': project}).fetchall()
    if result is not None:
        return [res[0] for res in result]


def passwordOperator(document):
    db = MyDB('register')
    result = db.query("SELECT password FROM operator WHERE document = :document", {'document': document}).fetchone()
    if result is not None:
        return result[0]


def projectsOperator(document):
    db = MyDB('register')
    result = db.query("SELECT fkProject FROM operatorProjects WHERE fkOperator = :document",
                      {'document': document}).fetchall()
    if result is not None:
        return [res[0] for res in result]


def nameProject(project):
    db = MyDB('register')
    result = db.query("SELECT name FROM projects WHERE id = :project", {'project': project}).fetchone()
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
    db.commit("INSERT INTO payee VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", info)


def loadPayeeProjects(info):
    db = MyDB('register')
    db.commit("INSERT INTO payeeProjects VALUES (?,?,?,?,?)", info)


def loadProductionProfileDiag(info):
    db = MyDB('register')
    db.commit("INSERT INTO productionProfileDiag VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?"
              ",?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", info)


def loadBussinesIdea(info):
    db = MyDB('register')
    db.commit("INSERT INTO bussinesIdea VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", info)
