from .. import db



class User(db.Model):
    __tablename__ = 'user_db'

    id = db.Column('user_id',db.String(10),primary_key=True)
    password=db.Column('user_password',db.String(20))
    phone=db.Column('user_phone',db.String(20))
    name=db.Column('user_name',db.String(20))
    card=db.Column('user_card',db.String(20))
    role=db.Column('user_role',db.Integer())

    def __init__(self, id, password,phone,name,card,role):
        self.id = id
        self.password = password
        self.phone = phone
        self.name = name
        self.card = card
        self.role = role

    def __repr__(self):
        return "<[User] username:`{}`, password:`{}`, phone:`{}`, name:`{}`, card:`{}`, role:`{}`".format(self.id, self.password,self.phone,self.name,self.card,self.role)
