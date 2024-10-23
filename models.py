from singleton_db import SingletonDB

db = SingletonDB().db

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(100), nullable=False)

class Prefix(db.Model):
    __tablename__ = 'prefixes'
    id = db.Column(db.Integer, primary_key=True)
    prefix = db.Column(db.String(100), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)

class Suffix(db.Model):
    __tablename__ = 'suffixes'
    id = db.Column(db.Integer, primary_key=True)
    suffix = db.Column(db.String(100), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
