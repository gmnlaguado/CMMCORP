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


db.create_all()


@app.route('/payee', methods=['POST'])
def add_beneficiario():
    info = request.json
    new_payee = payee(**info)
    db.session.add(new_payee)
    db.session.commit()
    return 'Complete'


if __name__ == "__main__":
    app.run(debug=True)
