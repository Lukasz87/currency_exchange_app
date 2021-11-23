from project_currency_exchange import create_app, db


def normal_run():
    """ val - True or False"""
    db.create_all(app=create_app())  # todo regenerate DB
    app = create_app()
    app.debug = True
    app.run()


if __name__ == '__main__':
    normal_run()
