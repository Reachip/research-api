import functools
import os 
import flask 
import jwt

def get_decoded_jwt(jwt):
    secret_jwt_key = os.environ.get("SECRET_JWT_KEY")
    return jwt.decode(jwt, secret_jwt_key)

def get_jwt(payload):
    secret_jwt_key = os.environ.get("SECRET_JWT_KEY")
    return jwt.encode(payload, secret_jwt_key).decode("utf-8")

def require_jwt(fn):
    @functools.wraps(fn)
    def wrapped(*args, **kwargs):
        if flask.request.headers["Authorization"]:
            try:
                supposed_token = flask.request.headers["Authorization"].split()[1]
                kwargs["decoded_token"] = jwt.decode(supposed_token, "my super secret key")
                return fn(*args, **kwargs)

            except jwt.ExpiredSignatureError:
                return {"message": "signature has expired"}

            except jwt.DecodeError:
                return {"message": "invalid token"}

            except IndexError:
                return {"message": "You need a token to use this part of the API"}

        return {"message": "You need a token to use this part of the API"}
    
    return wrapped