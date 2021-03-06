from flask import Flask, jsonify, render_template

from flask_restful import Api
from flask_jwt_extended import JWTManager

from tt.model import dbt
from tt import resources

from logging.config import dictConfig

dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s"
            }
        },
        "handlers": {
            "wsgi": {
                "class": "logging.StreamHandler",
                "stream": "ext://flask.logging.wsgi_errors_stream",
                "formatter": "default",
            }
        },
        "root": {"level": "DEBUG", "handlers": ["wsgi"]},
    }
)

app = Flask(__name__)

# app = Flask(__name__, static_url_path='/build')
app = Flask(
    __name__.split(".")[0],
    static_folder="client/build/static",
    template_folder="client/build",
)
api = Api(app)

app.config["JWT_SECRET_KEY"] = "boost-is-the-secret-of-our-app"
jwt = JWTManager(app)


@app.route("/")
def index():
    return render_template("index.html")


api.add_resource(resources.UserRegistration, "/register")
# api.add_resource(resources.UserLogin, '/login')

if __name__ == "__main__":
    app.debug = True
    app.run(threaded=True, port=5000)
