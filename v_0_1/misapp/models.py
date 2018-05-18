from .. import db



class User(db.Model):
    __tablename__ = 'user_db'

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    password=db.Column(db.String(20))
    phone=db.Column(db.String(20))
    name=db.Column(db.String(20))
    card=db.Column(db.String(20))
    role=db.Column(db.Integer)

    def __init__(self, id, password,phone,name,card,role):
        self.id = id
        self.password = password
        self.phone = phone
        self.name = name
        self.card = card
        self.role = role

    def __repr__(self):
        return "<[User] username:`{}`, password:`{}`, phone:`{}`, name:`{}`, card:`{}`, role:`{}`".format(self.id, self.password,self.phone,self.name,self.card,self.role)
