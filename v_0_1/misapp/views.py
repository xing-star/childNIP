from flask import request
from flask.views import MethodView
from flask import jsonify
from .models import *


class Index(MethodView):

    def __init__(self):
        pass

    def get(self):
        return 'hello'
