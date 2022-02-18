from flask_script import Manager,Server
from flask_migrate import Migrate,MigrateCommand


from app.main.v1.models.models import Orders, Pizza, Roles, Size, Toppings, User
from app import create_app,db

app = create_app('deveolpment')
manager = Manager(app)

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User,Roles = Roles,Pizza = Pizza,Size = Size,Toppings = Toppings,Orders = Orders)


if __name__ == '__main__':
    manager.run()