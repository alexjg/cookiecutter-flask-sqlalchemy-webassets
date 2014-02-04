import sys
from os import path
sys.path.append(path.dirname(path.dirname(__file__)))

from {{cookiecutter.package_name}} import app
app.debug = True
app.run()
