# coding=utf-8
import urllib
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from decouple import config

connection_string = 'Driver={' + config('db_driver') + '};Server=' + config('db_host') + ';Database=' + \
                    config('db_name') + ';UID=' + config('db_user') + ';PWD=' + config('db_password') + ';' + 'PORT=' \
                    + config('db_port') + ';'

string = urllib.parse.quote_plus(connection_string)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%scharset=utf8" % string
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class payee(db.Model):
    project = db.Column(db.String(255))
    names = db.Column(db.String(255))
    lastNames = db.Column(db.String(255))
    docType = db.Column(db.Integer)
    document = db.Column(db.String(255), primary_key=True)
    expeditionCity = db.Column(db.Integer)
    birthdate = db.Column(db.DateTime)
    city = db.Column(db.Integer)
    department = db.Column(db.Integer)
    country = db.Column(db.Integer)
    sign = db.Column(db.Integer)
    address = db.Column(db.String(255))
    neighborhood = db.Column(db.Integer)
    indicative = db.Column(db.Integer)
    telephone = db.Column(db.Integer)
    cellphone = db.Column(db.Integer)
    email = db.Column(db.String(255))
    operator = db.Column(db.String(255))
    cellphone2 = db.Column(db.Integer)
    payeeType = db.Column(db.Integer)
    date = db.Column(db.DateTime)
    ageRange = db.Column(db.Integer)
    nationality = db.Column(db.Integer)
    environment = db.Column(db.Integer)
    tier = db.Column(db.Integer)
    sex = db.Column(db.Integer)
    gender = db.Column(db.Integer)
    ethnicGroup = db.Column(db.Integer)
    disability = db.Column(db.Integer)

    def __init__(self, **kwargs):
        self.project = kwargs['project']
        self.names = kwargs['names']
        self.lastNames = kwargs['lastNames']
        self.docType = kwargs['docType']
        self.document = kwargs['document']
        self.expeditionCity = kwargs['expeditionCity']
        self.birthdate = kwargs['birthdate']
        self.city = kwargs['city']
        self.department = kwargs['department']
        self.country = kwargs['country']
        self.sign = kwargs['sign']
        self.address = kwargs['address']
        self.neighborhood = kwargs['neighborhood']
        self.indicative = kwargs['indicative']
        self.telephone = kwargs['telephone']
        self.cellphone = kwargs['cellphone']
        self.email = kwargs['email']
        self.operator = kwargs['operator']
        self.cellphone2 = kwargs['cellphone2']
        self.payeeType = kwargs['payeeType']
        self.date = kwargs['date']
        self.ageRange = kwargs['ageRange']
        self.nationality = kwargs['nationality']
        self.environment = kwargs['environment']
        self.tier = kwargs['tier']
        self.sex = kwargs['sex']
        self.gender = kwargs['gender']
        self.ethnicGroup = kwargs['ethnicGroup']
        self.disability = kwargs['disability']


class payee_projects(db.Model):
    id = db.Column(db.String(255), primary_key=True)
    project = db.Column(db.String(255))
    operator = db.Column(db.String(255))
    payeeDocument = db.Column(db.String(255))
    date = db.Column(db.DateTime)
    status = db.Column(db.Integer)

    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.project = kwargs['project']
        self.operator = kwargs['operator']
        self.payeeDocument = kwargs['payeeDocument']
        self.date = kwargs['date']
        self.status = kwargs['status']


class production_profile_diag(db.Model):
    payeeDocument = db.Column(db.String(255), primary_key=True)
    Field1 = db.Column(db.Integer)
    Field2 = db.Column(db.Integer)
    Field3 = db.Column(db.Integer)
    Field4 = db.Column(db.Integer)
    Field5 = db.Column(db.Integer)
    Field6 = db.Column(db.Integer)
    Field7 = db.Column(db.Integer)
    Field8 = db.Column(db.Integer)
    Field9 = db.Column(db.Integer)
    Field10 = db.Column(db.Integer)
    Field11 = db.Column(db.Integer)
    Field12 = db.Column(db.Integer)
    Field13 = db.Column(db.Integer)
    Field14 = db.Column(db.Integer)
    Field15 = db.Column(db.Integer)
    Field16 = db.Column(db.Integer)
    Field17 = db.Column(db.Integer)
    Field18 = db.Column(db.Integer)
    Field19 = db.Column(db.Integer)
    Field20 = db.Column(db.Integer)
    Field21 = db.Column(db.Integer)
    Field22 = db.Column(db.Integer)
    Field23 = db.Column(db.Integer)
    Field24 = db.Column(db.Integer)
    Field25 = db.Column(db.Integer)
    Field26 = db.Column(db.Integer)
    Field27 = db.Column(db.Integer)
    Field28 = db.Column(db.Integer)
    Field29 = db.Column(db.Integer)
    Field30 = db.Column(db.Integer)
    Field31 = db.Column(db.Integer)
    Field32 = db.Column(db.Integer)
    Field33 = db.Column(db.Integer)
    Field34 = db.Column(db.Integer)
    Field35 = db.Column(db.Integer)
    Field36 = db.Column(db.Integer)
    Field37 = db.Column(db.Integer)
    Field38 = db.Column(db.Integer)
    Field39 = db.Column(db.Integer)
    Field40 = db.Column(db.Integer)
    Field41 = db.Column(db.Integer)
    Field42 = db.Column(db.Integer)
    Field43 = db.Column(db.Integer)
    Field44 = db.Column(db.Integer)
    Field45 = db.Column(db.Integer)
    Field46 = db.Column(db.Integer)
    Field47 = db.Column(db.Integer)
    Field48 = db.Column(db.Integer)
    Field49 = db.Column(db.Integer)
    Field50 = db.Column(db.Integer)
    Field51 = db.Column(db.Integer)
    Field52 = db.Column(db.Integer)
    Field53 = db.Column(db.Integer)
    Field54 = db.Column(db.Integer)
    Field55 = db.Column(db.Integer)
    Field56 = db.Column(db.Integer)
    Field57 = db.Column(db.Integer)
    Field58 = db.Column(db.Integer)
    Field59 = db.Column(db.Integer)
    Field60 = db.Column(db.Integer)
    Field61 = db.Column(db.Integer)
    Field62 = db.Column(db.Integer)
    Field63 = db.Column(db.Integer)
    Field64 = db.Column(db.Integer)
    Field65 = db.Column(db.Integer)
    Field66 = db.Column(db.Integer)
    Field67 = db.Column(db.Integer)
    Field68 = db.Column(db.Integer)
    Field69 = db.Column(db.Integer)
    Field70 = db.Column(db.Integer)

    def __init__(self, **kwargs):
        self.payeeDocument = kwargs['payeeDocument']
        self.Field1 = kwargs['Field1']
        self.Field2 = kwargs['Field2']
        self.Field3 = kwargs['Field3']
        self.Field4 = kwargs['Field4']
        self.Field5 = kwargs['Field5']
        self.Field6 = kwargs['Field6']
        self.Field7 = kwargs['Field7']
        self.Field8 = kwargs['Field8']
        self.Field9 = kwargs['Field9']
        self.Field10 = kwargs['Field10']
        self.Field11 = kwargs['Field11']
        self.Field12 = kwargs['Field12']
        self.Field13 = kwargs['Field13']
        self.Field14 = kwargs['Field14']
        self.Field15 = kwargs['Field15']
        self.Field16 = kwargs['Field16']
        self.Field17 = kwargs['Field17']
        self.Field18 = kwargs['Field18']
        self.Field19 = kwargs['Field19']
        self.Field20 = kwargs['Field20']
        self.Field21 = kwargs['Field21']
        self.Field22 = kwargs['Field22']
        self.Field23 = kwargs['Field23']
        self.Field24 = kwargs['Field24']
        self.Field25 = kwargs['Field25']
        self.Field26 = kwargs['Field26']
        self.Field27 = kwargs['Field27']
        self.Field28 = kwargs['Field28']
        self.Field29 = kwargs['Field29']
        self.Field30 = kwargs['Field30']
        self.Field31 = kwargs['Field31']
        self.Field32 = kwargs['Field32']
        self.Field33 = kwargs['Field33']
        self.Field34 = kwargs['Field34']
        self.Field35 = kwargs['Field35']
        self.Field36 = kwargs['Field36']
        self.Field37 = kwargs['Field37']
        self.Field38 = kwargs['Field38']
        self.Field39 = kwargs['Field39']
        self.Field40 = kwargs['Field40']
        self.Field41 = kwargs['Field41']
        self.Field42 = kwargs['Field42']
        self.Field43 = kwargs['Field43']
        self.Field44 = kwargs['Field44']
        self.Field45 = kwargs['Field45']
        self.Field46 = kwargs['Field46']
        self.Field47 = kwargs['Field47']
        self.Field48 = kwargs['Field48']
        self.Field49 = kwargs['Field49']
        self.Field50 = kwargs['Field50']
        self.Field51 = kwargs['Field51']
        self.Field52 = kwargs['Field52']
        self.Field53 = kwargs['Field53']
        self.Field54 = kwargs['Field54']
        self.Field55 = kwargs['Field55']
        self.Field56 = kwargs['Field56']
        self.Field57 = kwargs['Field57']
        self.Field58 = kwargs['Field58']
        self.Field59 = kwargs['Field59']
        self.Field60 = kwargs['Field60']
        self.Field61 = kwargs['Field61']
        self.Field62 = kwargs['Field62']
        self.Field63 = kwargs['Field63']
        self.Field64 = kwargs['Field64']
        self.Field65 = kwargs['Field65']
        self.Field66 = kwargs['Field66']
        self.Field67 = kwargs['Field67']
        self.Field68 = kwargs['Field68']
        self.Field69 = kwargs['Field69']
        self.Field70 = kwargs['Field70']

class production_profile_diag(db.Model):

db.create_all()




@app.route('/payee', methods=['POST'])
def add_payee():
    info = request.json
    new_payee = payee(**info)
    db.session.add(new_payee)
    db.session.commit()
    return 'Complete payee'


@app.route('/payee_projects', methods=['POST'])
def add_payee_projects():
    info = request.json
    new_payee_projects = payee_projects(**info)
    db.session.add(new_payee_projects)
    db.session.commit()
    return 'Complete payee_projects'


@app.route('/production_profile_diag', methods=['POST'])
def add_production_profile_diag():
    info = request.json
    new_production_profile_diag = production_profile_diag(**info)
    db.session.add(new_production_profile_diag)
    db.session.commit()
    return 'Complete production_profile_diag'


if __name__ == "__main__":
    app.run(debug=True)
