import json
from flask_restful import Resource, reqparse
from playhouse.shortcuts import model_to_dict
from ...models.navigation.reports import NavigationReports as NavigationReportsModel


class NavigationReports(Resource):
    def get(self):
        output = []
        parser = reqparse.RequestParser()
        parser.add_argument("limit", type=int)
        parser.add_argument("start", type=int)
        args = parser.parse_args()
        
        print(args["limit"])

        reports = NavigationReportsModel.select().where(
            (NavigationReportsModel.id >= args["start"])
        ).order_by(NavigationReportsModel.timestamp).limit(args["limit"])

        for report in reports:
            output.append(
                model_to_dict(report)
            )
            
        return output