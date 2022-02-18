from app import db
from app import ma
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class User(db.Model):
    """This will define all behaviours of the user

    Args:
        db ([type]): [description]
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))
    location = db.Column(db.String(255))
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))

    def __repr__(self):
        return f'User {self.username}'

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User 
        # load_instance = True


class Roles(db.Model):
    """This defines the users roles

    Args:
        db ([type]): [description]
    """
    __tablename__ = 'roles'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'roles',lazy="dynamic")

class Pizza(db.Model):
    """This defines the behaviours of an individual pizza

    Args:
        db ([type]): [description]
    """
    __tablename__ = 'pizza'
    id = db.Column(db.Integer,primary_key = True)
    name= db.Column(db.String(255))
    base_price = db.Column(db.Integer)

class Size(db.Model):
    """This will define the aspects of size

    Args:
        db ([type]): [description]
    """
    __tablename__ = 'size'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    price = db.Column(db.Integer)

class Toppings(db.Model):
    """This will define the topping aspects

    Args:
        db ([type]): [description]
    """
    __tablename__ = 'toppings'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    price = db.Column(db.Integer)

class Orders(db.Model):
    """This is 

    Args:
        db ([type]): [description]
    """
    __tablename__ = 'orders'
    id = db.Column(db.Integer,primary_key = True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    pizza_id = db.Column(db.Integer,db.ForeignKey('pizza.id'))
    size_id = db.Column(db.Integer,db.ForeignKey('size.id'))
    topping_id = db.Column(db.Integer,db.ForeignKey('toppings.id'))
    price = db.Column(db.Integer)
    quantity = db.Column(db.Integer)