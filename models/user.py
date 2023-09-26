from db import db


class UserModel(db.Model):
    __tablename__ = 'users'

    userid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    # items = db.relationship('ItemModel', lazy='dynamic')  # to access this column items.all()

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def json(self):
        return {'name': self.username, 'stores': [item.json() for item in self.items.all()]}

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(name=username).first()

    @classmethod
    def find_by_userid(cls, userid):
        return cls.query.filter_by(userid=userid).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()