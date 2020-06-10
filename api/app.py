# coding=utf-8
from flask import Flask, request
import pymssql


class MyDB(object):
    def __init__(self):
        db_host = '190.145.94.91'
        db_name = 'CMMRSocial'
        db_user = 'Arnulforojas'
        db_password = 'Arojas032020'
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
    return '<h1>Deployed CMM application</h1>'


@app.route('/payee', methods=['POST'])
def add_payee():
    payee_info = request.json
    info = []
    for item in payee_info.values():
        info.append(item)
    info = tuple(info)
    query = "INSERT INTO payee VALUES ('%s','%s','%s',%s,'%s',%s,'%s',%s,%s,%s,%s,'%s',%s,%s,%s,%s,'%s','%s',%s,%s," \
            "'%s',%s,%s,%s,%s,%s,%s,%s,%s)" % info
    db = MyDB()
    db.commit(query)
    return f'Complete payee query:\n{query}'


@app.route('/payee_projects', methods=['POST'])
def add_payee_projects():
    return 'Complete payee_projects'


@app.route('/production_profile_diag', methods=['POST'])
def add_production_profile_diag():
    return 'Complete production_profile_diag'


@app.route('/bussines_idea', methods=['POST'])
def add_bussines_idea():
    return 'Complete bussines_idea'


@app.route('/bussines_unit', methods=['POST'])
def add_bussines_unit():
    return 'Complete bussines_unit'


if __name__ == "__main__":
    app.run()

