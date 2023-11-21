'''
You need to run init-db to create the database in the instance folder:
    flask --app blog init-db
'''

import os

from flask import Flask


def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    
    db_path = os.path.join(app.instance_path, 'blog.sqlite')
    
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY='dev',
        # store the database in the instance folder
        DATABASE=db_path,
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    # check if database exists, if not initialise it 
    if not os.path.isfile(db_path):
        with app.app_context():
            from . import db
            db.init_db()
            print("Initialized the database.")

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    
    # register the database commands
    from . import db
    db.init_app(app)
    
    # apply the blueprints to the app
    from . import auth
    app.register_blueprint(auth.bp)
    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app