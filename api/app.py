# coding=utf-8
from logging import info
from flask import Flask, request
import os
import pymssql

class MyDB(object):
    def __init__(self):
        db_host = '190.145.94.93'
        db_name = 'CMMCRSocial'
        db_user = 'GeorgeNino'
        db_password = 'Gmnino@2021'
        self._db_connection = pymssql.connect(server=db_host, user=db_user, password=db_password, database=db_name)
        self._db_cur = self._db_connection.cursor()

    def commit(self, query):
        self._db_cur.execute(query)
        return self._db_connection.commit()
    
    def commit_many(self, table, values):
        self._db_cur.executemany(f'INSERT OR REPLACE INTO {table} VALUES ({values})')

    def parametricQuery(self, query):
        return self._db_cur.execute(query)

    def __del__(self):
        self._db_connection.close()

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Información Operarios</h1>'


@app.route('/actividad_implementacion', methods=['POST'])
def actividad_implementacion():
    informacion = request.json
    data = informacion['actividad_implementacion']
    cols = informacion['cols']
    db = MyDB()
    for row in data:
        pos = 0
        ajuste = ''
        for info in row:
            if (pos + 1) == len(cols):
                ajuste += f"{cols[pos]} = '{info}'"
            elif not cols[pos] == 'id':
                ajuste += f"{cols[pos]} = '{info}', "
            else:
                id = info
            pos += 1

        try:
            query = f"INSERT INTO actividad_implementacion VALUES {tuple(row)}"
            db.commit(query)
        except:
            query = f"UPDATE [actividad_implementacion] SET {ajuste}"
            db.commit(query)
    return f'actividad_implementacion\n\n'


@app.route('/actividad_seguimiento', methods=['POST'])
def actividad_seguimiento():
    informacion = request.json
    data = informacion['actividad_seguimiento']
    cols = informacion['cols']
    db = MyDB()
    for row in data:
        pos = 0
        ajuste = ''
        for info in row:
            if (pos + 1) == len(cols):
                ajuste += f"{cols[pos]} = '{info}'"
            elif not cols[pos] == 'id':
                ajuste += f"{cols[pos]} = '{info}', "
            else:
                id = info
            pos += 1

        try:
            query = f"INSERT INTO actividad_seguimiento VALUES {tuple(row)}"
            db.commit(query)
        except:
            query = f"UPDATE [actividad_seguimiento] SET {ajuste}"
            db.commit(query)
    return f'actividad_seguimiento\n\n'


@app.route('/beneficiario_proyectos', methods=['POST'])
def beneficiario_proyectos():
    informacion = request.json
    data = informacion['beneficiario_proyectos']
    cols = informacion['cols']
    db = MyDB()
    for row in data:
        pos = 0
        ajuste = ''
        for info in row:
            if (pos + 1) == len(cols):
                ajuste += f"{cols[pos]} = '{info}'"
            elif not cols[pos] == 'id':
                ajuste += f"{cols[pos]} = '{info}', "
            else:
                id = str(info)
            pos += 1

        try:
            query = f"INSERT INTO beneficiario_proyectos VALUES {tuple(row)}"
            db.commit(query)
        except:
            query = f"UPDATE [beneficiario_proyectos] SET {ajuste}"
            db.commit(query)
    return f'beneficiario_proyectos\n\n'


@app.route('/caracterizacion_ampliada', methods=['POST'])
def caracterizacion_ampliada():
    informacion = request.json
    data = informacion['caracterizacion_ampliada']
    cols = informacion['cols']
    db = MyDB()
    for row in data:
        pos = 0
        ajuste = ''
        for info in row:
            if (pos + 1) == len(cols):
                ajuste += f"{cols[pos]} = '{info}'"
            elif not cols[pos] == 'id':
                ajuste += f"{cols[pos]} = '{info}', "
            else:
                id = info
            pos += 1

        try:
            query = f"INSERT INTO caracterizacion_ampliada VALUES {tuple(row)}"
            db.commit(query)
        except:
            query = f"UPDATE [caracterizacion_ampliada] SET {ajuste}"
            db.commit(query)
    return f'caracterizacion_ampliada\n\n'


@app.route('/caracterizacion_ampliada_informacion_hijos', methods=['POST'])
def caracterizacion_ampliada_informacion_hijos():
    informacion = request.json
    data = informacion['caracterizacion_ampliada_informacion_hijos']
    cols = informacion['cols']
    db = MyDB()
    for row in data:
        pos = 0
        ajuste = ''
        for info in row:
            if (pos + 1) == len(cols):
                ajuste += f"{cols[pos]} = '{info}'"
            elif not cols[pos] == 'id':
                ajuste += f"{cols[pos]} = '{info}', "
            else:
                id = info
            pos += 1

        try:
            query = f"INSERT INTO caracterizacion_ampliada_informacion_hijos VALUES {tuple(row)}"
            db.commit(query)
        except:
            query = f"UPDATE [caracterizacion_ampliada_informacion_hijos] SET {ajuste}"
            db.commit(query)
    return f'caracterizacion_ampliada_informacion_hijos\n\n'



@app.route('/caracterizacion_ampliada_informacion_personas_a_cargo', methods=['POST'])
def caracterizacion_ampliada_informacion_personas_a_cargo():
    informacion = request.json
    data = informacion['caracterizacion_ampliada_informacion_personas_a_cargo']
    cols = informacion['cols']
    db = MyDB()
    for row in data:
        pos = 0
        ajuste = ''
        for info in row:
            if (pos + 1) == len(cols):
                ajuste += f"{cols[pos]} = '{info}'"
            elif not cols[pos] == 'id':
                ajuste += f"{cols[pos]} = '{info}', "
            else:
                id = info
            pos += 1

        try:
            query = f"INSERT INTO caracterizacion_ampliada_informacion_personas_a_cargo VALUES {tuple(row)}"
            db.commit(query)
        except:
            query = f"UPDATE [caracterizacion_ampliada_informacion_personas_a_cargo] SET {ajuste}"
            db.commit(query)
    return f'caracterizacion_ampliada_informacion_personas_a_cargo\n\n'


@app.route('/diagnostico_de_perfil_productivo', methods=['POST'])
def diagnostico_de_perfil_productivo():
    informacion = request.json
    data = informacion['diagnostico_de_perfil_productivo']
    cols = informacion['cols']
    db = MyDB()
    for row in data:
        pos = 0
        ajuste = ''
        for info in row:
            if (pos + 1) == len(cols):
                ajuste += f"{cols[pos]} = '{info}'"
            elif not cols[pos] == 'document':
                ajuste += f"{cols[pos]} = '{info}', "
            else:
                document = info
            pos += 1

        try:
            query = f"INSERT INTO diagnostico_de_perfil_productivo VALUES {tuple(row)}"
            db.commit(query)
        except:
            query = f"UPDATE [diagnostico_de_perfil_productivo] SET {ajuste} where document = {document}"
            db.commit(query)
    return f'diagnostico_de_perfil_productivo\n\n'


@app.route('/diagnostico_empresarial', methods=['POST'])
def diagnostico_empresarial():
    informacion = request.json
    data = informacion['diagnostico_empresarial']
    cols = informacion['cols']
    db = MyDB()
    for row in data:
        pos = 0
        ajuste = ''
        for info in row:
            if (pos + 1) == len(cols):
                ajuste += f"{cols[pos]} = '{info}'"
            elif not cols[pos] == 'id':
                ajuste += f"{cols[pos]} = '{info}', "
            else:
                id = info
            pos += 1

        try:
            query = f"INSERT INTO diagnostico_empresarial VALUES {tuple(row)}"
            db.commit(query)
        except:
            query = f"UPDATE [diagnostico_empresarial] SET {ajuste}"
            db.commit(query)
    return f'diagnostico_empresarial\n\n'


@app.route('/idea_de_negocio', methods=['POST'])
def idea_de_negocio():
    informacion = request.json
    data = informacion['idea_de_negocio']
    cols = informacion['cols']
    db = MyDB()
    for row in data:
        pos = 0
        ajuste = ''
        for info in row:
            if (pos + 1) == len(cols):
                ajuste += f"{cols[pos]} = '{info}'"
            elif not cols[pos] == 'id':
                ajuste += f"{cols[pos]} = '{info}', "
            else:
                id = info
            pos += 1

        try:
            query = f"INSERT INTO idea_de_negocio VALUES {tuple(row)}"
            db.commit(query)
        except:
            query = f"UPDATE [idea_de_negocio] SET {ajuste}"
            db.commit(query)
    return f'idea_de_negocio\n\n'


@app.route('/informacion_general_beneficiario', methods=['POST'])
def informacion_general_beneficiario():
    informacion = request.json
    data = informacion['informacion_general_beneficiario']
    cols = informacion['cols']
    db = MyDB()
    for row in data:
        pos = 0
        ajuste = ''
        for info in row:    
            if (pos + 1) == len(cols):
                ajuste += f"{cols[pos]} = '{info}'"
            elif not cols[pos] == 'document':
                ajuste += f"{cols[pos]} = '{info}', "
            else:
                document = info
            pos += 1

        try:
            query = f"INSERT INTO informacion_general_beneficiario VALUES {tuple(row)}"
            db.commit(query)
        except:
            query = f"UPDATE [informacion_general_beneficiario] SET {ajuste} where document = {document}"
            db.commit(query)
    return f'informacion_general_beneficiario\n\n'


@app.route('/monitoreo', methods=['POST'])
def monitoreo():
    informacion = request.json
    data = informacion['monitoreo']
    cols = informacion['cols']
    db = MyDB()
    for row in data:
        pos = 0
        ajuste = ''
        for info in row:
            if (pos + 1) == len(cols):
                ajuste += f"{cols[pos]} = '{info}'"
            elif not cols[pos] == 'id':
                ajuste += f"{cols[pos]} = '{info}', "
            else:
                id = info
            pos += 1

        try:
            query = f"INSERT INTO monitoreo VALUES {tuple(row)}"
            db.commit(query)

        except:
            query = f"UPDATE [monitoreo] SET {ajuste}"
            db.commit(query)
    return f'monitoreo\n\n'


'''
@app.route('/odp_operario', methods=['POST'])
def odp_operario():
    informacion = request.json
    info = []
    for item in informacion.values():
        info.append(item)
    info = tuple(info)
    query = "INSERT OR REPLACE INTO odp_operario VALUES ('%s','%s','%s','%s',%s)" % info
    db = MyDB()
    db.commit(query)
    return f'odp_operario\n\n{query}'


@app.route('/odp_operario_proyectos', methods=['POST'])
def odp_operario_proyectos():
    informacion = request.json
    info = []
    for item in informacion.values():
        info.append(item)
    info = tuple(info)
    query = "INSERT OR REPLACE INTO odp_operario_proyectos VALUES ('%s','%s','%s')" % info
    db = MyDB()
    db.commit(query)
    return f'odp_operario_proyectos\n\n{query}'
'''


@app.route('/plan_de_formacion', methods=['POST'])
def plan_de_formacion():
    informacion = request.json
    data = informacion['plan_de_formacion']
    cols = informacion['cols']
    db = MyDB()
    for row in data:
        pos = 0
        ajuste = ''
        for info in row:
            if (pos + 1) == len(cols):
                ajuste += f"{cols[pos]} = '{info}'"
            elif not cols[pos] == 'id':
                ajuste += f"{cols[pos]} = '{info}', "
            else:
                id = info
            pos += 1

        try:
            query = f"INSERT INTO plan_de_formacion VALUES {tuple(row)}"
            db.commit(query)
        except:
            query = f"UPDATE [plan_de_formacion] SET {ajuste}"
            db.commit(query)
    return f'plan_de_formacion\n\n'


@app.route('/plan_de_implementacion', methods=['POST'])
def plan_de_implementacion():
    informacion = request.json
    data = informacion['plan_de_implementacion']
    cols = informacion['cols']
    db = MyDB()
    for row in data:
        pos = 0
        ajuste = ''
        for info in row:
            if (pos + 1) == len(cols):
                ajuste += f"{cols[pos]} = '{info}'"
            elif not cols[pos] == 'id':
                ajuste += f"{cols[pos]} = '{info}', "
            else:
                id = info
            pos += 1

        try:
            query = f"INSERT INTO plan_de_implementacion VALUES {tuple(row)}"
            db.commit(query)
        except:
            query = f"UPDATE [plan_de_implementacion] SET {ajuste}"
            db.commit(query)
    return f'plan_de_implementacion\n\n'


@app.route('/plan_de_seguimiento', methods=['POST'])
def plan_de_seguimiento():
    informacion = request.json
    data = informacion['plan_de_seguimiento']
    cols = informacion['cols']
    db = MyDB()
    for row in data:
        pos = 0
        ajuste = ''
        for info in row:
            if (pos + 1) == len(cols):
                ajuste += f"{cols[pos]} = '{info}'"
            elif not cols[pos] == 'id':
                ajuste += f"{cols[pos]} = '{info}', "
            else:
                id = info
            pos += 1

        try:
            query = f"INSERT INTO plan_de_seguimiento VALUES {tuple(row)}"
            db.commit(query)
        except:
            query = f"UPDATE [plan_de_seguimiento] SET {ajuste}"
            db.commit(query)
    return f'plan_de_seguimiento\n\n'

'''
@app.route('/proyectos', methods=['POST'])
def proyectos():
    informacion = request.json
    info = []
    for item in informacion.values():
        info.append(item)
    info = tuple(info)
    query = "INSERT OR REPLACE INTO proyectos VALUES ('%s','%s','%s')" % info
    db = MyDB()
    db.commit(query)
    return f'proyectos\n\n{query}'

'''

@app.route('/unidad_de_negocio', methods=['POST'])
def unidad_de_negocio():
    informacion = request.json
    data = informacion['unidad_de_negocio']
    cols = informacion['cols']
    db = MyDB()
    for row in data:
        pos = 0
        ajuste = ''
        for info in row:
            if (pos + 1) == len(cols):
                ajuste += f"{cols[pos]} = '{info}'"
            elif not cols[pos] == 'id':
                ajuste += f"{cols[pos]} = '{info}', "
            else:
                id = info
            pos += 1

        try:
            query = f"INSERT INTO unidad_de_negocio VALUES {tuple(row)}"
            db.commit(query)
        except:
            query = f"UPDATE [unidad_de_negocio] SET {ajuste}"
            db.commit(query)
    return f'unidad_de_negocio\n\n'


@app.route('/obtener_operarios', methods=['POST'])
def obtener_operarios():
    db = MyDB()
    db.parametricQuery("SELECT document, name, username, password FROM odp_operario")
    result = db._db_cur.fetchall()
    return f'{result}'
    

@app.route('/obtener_operarios_proyectos', methods=['POST'])
def obtener_operarios_proyectos():
    db = MyDB()
    db.parametricQuery("SELECT id, fkOperator, fkProject FROM odp_operario_proyectos")
    result = db._db_cur.fetchall()
    return f'{result}'

@app.route('/obtener_datos/<table>', methods=['GET'])
def obtener_datos(table):
    db = MyDB()
    db.parametricQuery("SELECT * FROM %s" % table)
    result = db._db_cur.fetchall()
    response = {
        table: result
    }
    return response


if __name__ == "__main__":
    app.run(host= '0.0.0.0')

