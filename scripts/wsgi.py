#from app import flask_app
import os
import sys
from werkzeug.wsgi import DispatcherMiddleware
from werkzeug.exceptions import NotFound

from app import flask_app

#if __name__ == "__main__":
app = DispatcherMiddleware(flask_app())    
#app.run()

