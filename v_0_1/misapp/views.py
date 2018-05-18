from flask import request
from flask.views import MethodView
from .models import *


class Index(MethodView):

    def __init__(self):
        pass

    @staticmethod
    def get():
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


class Add(MethodView):

    def __init__(self):
        self.phone = request.form.get('user_phone')
        self.pwd = request.form.get('pwd')

    def post(self):
        user = User(id='5555', password=self.pwd, phone=self.phone, name='0', card='0', role='0')
        db.session.add(user)
        db.session.commit()
        # 此处如返回汉字，curl终端会乱码，此处不做处理。
        return "register success"


class Update(MethodView):

    def __init__(self):
        self.phone = request.form.get('user_phone')
        self.pwd = request.form.get('pwd')

    def put(self):
        result = User.query.filter_by(phone=self.phone).first()
        result.phone = '456'
        db.session.add(result)
        db.session.commit()
        return 'update success'


class Delete(MethodView):

    def __init__(self):
        self.phone = request.form.get('user_phone')

    def delete(self):
        result = User.query.filter_by(phone=self.phone).first()
        db.session.delete(result)
        db.session.commit()
        return "delete success"

