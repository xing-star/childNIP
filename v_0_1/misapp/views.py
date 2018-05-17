from flask import request
from flask.views import MethodView
from flask import jsonify
from .models import *


class Index(MethodView):

    def __init__(self):
        pass

    @staticmethod
    def get(self):
        return 'hello world!!!'


class Query(MethodView):

    def __init__(self):
        self.phone = request.args.get('user_phone')
        self.pwd = request.args.get('pwd')

    def get(self):
        user = User.query.filter_by(phone=self.phone).first()
        if user:
            pwd = User.query.filter_by(password=self.pwd).first()
            if pwd:
                return "登录成功"
            return '没有此用户或密码错误'
        return '没有此用户或密码错误'





