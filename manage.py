from app import create_app,db
from flask_script import Manager,Server
# from app.models import User
# from flask_migrate import Migrate, MigrateCommand

# Creating app instance
app = create_app('development')
# app = create_app('test')

manager = Manager(app)
manager.add_command('server',Server)


if __name__ == '__main__':
    manager.run()