from flask import Flask
from flask import request
import jwt

from flask_restful import Resource, reqparse, Api

from models import db
from models.users import Users
from models.navigation.reports import NavigationReports as NavigationReportModel
from resources.users import UserAuth, UserRegister
from resources.navigation.reports import NavigationReports as NavigationReportsRessource

app = Flask(__name__)
db.connect()
db.create_tables([Users, NavigationReportModel])

@app.after_request
def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = "*"
    response.headers['Access-Control-Allow-Methods'] = "POST, GET, OPTIONS, PUT, DELETE, PATCH"
    response.headers['Access-Control-Allow-Headers'] = "origin, content-type, accept, x-requested-with"
    return response

api = Api(app=app, prefix="/api")
api.add_resource(UserAuth, "/auth")
api.add_resource(UserRegister, "/register")
api.add_resource(NavigationReportsRessource, "/navigation/reports")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
