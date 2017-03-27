from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer(), primary_key=True)

    def save(self):
        db.session.add(self)
        db.session.commit()


class User(Base):
    __tablename__ = 'user'

    email = db.Column(db.String(100), unique=True)
    username = db.Column(db.String(50), unique=True, nullable=True)
    password = db.Column(db.String(150))
    entries = db.relationship('Entry', backref='user', lazy='dynamic')

    def __repr__(self):
        return '<User: {}>'.format(self.username)


class Entry(Base):
    __tablename__ = "entry"

    name = db.Column(db.String(200))
    creator_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
