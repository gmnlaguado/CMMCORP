# coding=utf-8
from flask import Flask, request
import pymssql
import os

API_USUARIO = os.environ.get('Usuario_Api')
API_CONTRASENA = os.environ.get('Contrasena_Api')
API_BASE_DE_DATOS = os.environ.get('Base_Datos_Api)


class MyDB(object):
    def __init__(self):
        db_host = '127.0.0.1'
        db_name = API_BASE_DE_DATOS
        db_user = API_USUARIO
        db_password = API_CONTRASENA
        self._db_connection = pymssql.connect(server=db_host, user=db_user, password=db_password, database=db_name)
        self._db_cur = self._db_connection.cursor()

    def commit(self, query):
        self._db_cur.execute(query)
        return self._db_connection.commit()

    def __del__(self):
        self._db_connection.close()


app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    return '<h1>Aplicación de la corporación en línea</h1>'


@app.route('/informacion_general', methods=['POST'])
def add_payee():
    payee_info = request.json
    return f'{payee_info}'


@app.route('/beneficiario_proyectos', methods=['POST'])
def add_payee_projects():
    return 'Complete payee_projects'


@app.route('/diagnostico_de_perfil_productivo', methods=['POST'])
def add_production_profile_diag():
    return 'Complete production_profile_diag'


@app.route('/idea_de_negocio', methods=['POST'])
def add_bussines_idea():
    return 'Complete bussines_idea'


@app.route('/unidad_de_negocio', methods=['POST'])
def add_bussines_unit():
    return 'Complete bussines_unit'


if __name__ == "__main__":
    app.run()

