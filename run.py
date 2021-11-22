from project_currency_exchange import create_app, db
if __name__ == '__main__':
    # db.create_all(app=create_app())     # todo regenerate DB

    app = create_app()
    app.debug = True
    app.run()
