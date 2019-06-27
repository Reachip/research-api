from flask_restful import Resource, reqparse
from models.navigation.reports import NavigationReports as NavigationReportsModel

class NavigationReports(Resource):
    def get(self):
        return {"TO": "DO"}