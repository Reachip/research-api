from flask_restful import Resource, reqparse
from flask import Response
import jwt 

from models.users import Users
from utils.jwt import get_jwt

class UserAuth(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("username", type=str)
        parser.add_argument("password", type=str)
        args = parser.parse_args(strict=True)
        
        query = Users.select().where((args["username"] == Users.username) & (args["password"] == Users.password))
        
        if query.exists():
            payload = {"username": args["username"], "role": query[0].role}
            token = get_jwt(payload)
            return {"access_token": token}

class UserRegister(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("username", type=str)
        parser.add_argument("password", type=str)
        parser.add_argument("mail", type=str)

        args = parser.parse_args(strict=True)
        query = Users.select().where(Users.mail == args["mail"])

        if not query.exists():
            Users.create(username=args["username"], mail=args["mail"], password=args["password"])
            return Response('{"message": "Succesfully registered"}', status=200)

        return Response('{"message": "email already taken"}', status=401)


