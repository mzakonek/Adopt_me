# from flask_script import Manager
# from flask_migrate import Migrate, MigrateCommand
#
# from app import app, db
#
# migrate = Migrate(app, db)
#
# manager = Manager(app)
# manager.add_command('db', MigrateCommand)
#
# .
# if __name__ == '__main__':
#     manager.run()

from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


server = Flask(__name__)
server.config.from_object(Config)
db.init_app(server)

migrate = Migrate(server, db)
manager = Manager(server)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()