from app.models import Entry, User, db
from app.views import app
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

db.init_app(app)
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


@manager.shell
def make_shell_context():
    return dict(
        app=app, db=db, Entry=Entry, User=User
    )
if __name__ == '__main__':
    manager.run()
