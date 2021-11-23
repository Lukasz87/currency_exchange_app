from project_currency_exchange import create_app, db
from flask_migrate import Migrate


def normal_run(val):
    """ val - True or False"""
    if val:
        db.create_all(app=create_app())  # todo regenerate DB
        app = create_app()
        app.debug = True
        app.run()
    else:
        app = create_app()
        migrate = Migrate(app, db)


if __name__ == '__main__':
    normal_run(False)
