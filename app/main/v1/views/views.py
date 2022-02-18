
from flask import jsonify,request
from flask_restful import Resource
from flask_restful.reqparse import RequestParser
from app.main.v1.models.models import User,UserSchema
from app import db

parser = RequestParser()
parser.add_argument('username',type=str,required=True,help='Please Enter your name')
parser.add_argument('email',type=str,required=True,help='Please input your email')
parser.add_argument('location',type=str,required=True,help='Please Enter where you live')

class ViewUser(Resource):
    def get(self):
        user = User.query.all()
        user_schema = UserSchema(many = True)
        output = user_schema.dump(user)
        
        return { 'user' : output}
    
    def post(self):
        args = parser.parse_args()
        args = request.get_json()
        email = args['email']
        username = args['username']
        password = args['password']
        location = args['location']

        new_user = User(username = username,email = email,password = password, location = location)
        db.session.add(new_user)
        db.session.commit()
        user = User.query.all()
        user_schema = UserSchema(many = True)
        output = user_schema.dump(user)

        return jsonify({ 'user' : output })

