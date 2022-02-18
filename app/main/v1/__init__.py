from flask import Blueprint,jsonify
from flask_restful import Api, Resource

main = Blueprint('main',__name__,url_prefix='/main')
api = Api(main,catch_all_404s=True)

class HelloWorld(Resource):
    def get (self):
        return {'hello':'world'}

api.add_resource(HelloWorld,'/')


from app.main.v1.views.views import ViewUser

api.add_resource(ViewUser,"/user")
