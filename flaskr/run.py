from flask import (Flask)
from flask_cors import CORS
from .controller.nutrition import nutrition_page
from .controller.hello import hello_page
from .controller.message import message_page

app = Flask("__main__")
app.register_blueprint(nutrition_page)
app.register_blueprint(hello_page)
app.register_blueprint(message_page)

CORS(app)
