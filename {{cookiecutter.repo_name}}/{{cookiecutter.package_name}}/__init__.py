import flask
from flask import request
from flask.ext import assets
from flask.ext.sqlalchemy import SQLAlchemy
import json
import logging.config
import os

import importlib
settings_module_name = os.environ.get("{{cookiecutter.package_name|upper}}_SETTINGS_MODULE", "{{cookiecutter.package_name}}.settings.development")
settings = importlib.import_module(settings_module_name)
logging.config.dictConfig(settings.LOGGING)

app = flask.Flask(__name__)
app.config.from_object(settings)
env = assets.Environment(app)

db = SQLAlchemy(app)
from . import models

vendor_js = assets.Bundle(
    "bower_components/jquery/jquery.js",
    "bower_components/foundation/js/foundation.js",
)

vendor_css = assets.Bundle(
    #"bower_components/jcsdl/minified/jcsdl.min.css"
)

app_css = assets.Bundle(
    "sass/app.scss",
    filters=("scss",),
    depends=("sass/*.scss"),
    output="app.css",
)
app_js = assets.Bundle(
    "coffee/*.coffee",
    filters=("coffeescript",),
    output="app.js"
)

env.register("vendor_js", vendor_js)
env.register("vendor_css", vendor_css)
env.register("app_css", app_css)
env.register("app_js", app_js)


@app.route("/")
def index():
    return flask.render_template("base.html")
