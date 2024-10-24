from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        DEBUG = True,
        SECRET_KEY = 'dev',
        SQLALCHEMY_DATABASE_URI = "mysql://root:1234@127.0.0.1:3306/todoapp"
    )

    db.init_app(app)

    from . import toDo
    app.register_blueprint(toDo.bp)
    
    from . import auth
    app.register_blueprint(auth.bp)

    @app.route("/")
    def index():
        return render_template('index.html')
    
    with app.app_context():
        db.create_all()
    
    return app