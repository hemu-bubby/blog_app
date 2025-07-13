from utils.db import db


class Author(db.Model):
    author_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    country = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(10), nullable=False)


class Blog(db.Model):
    blog_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, server_default=db.func.current_timestamp())
    author_id = db.Column(db.Integer, db.ForeignKey('author.author_id'), nullable=False)
    author = db.relationship('Author', backref=db.backref('blogs', lazy=True))
