#this will be used to store our database models
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from . import db
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(1000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # Ensure 'user' table exist
    
#User table
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    notes = db.relationship('Note')

#BoardGame table
class BoardGame(db.Model):
    __tablename__ = 'board_game'
    game_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    image = db.Column(db.String(255))

#BoardGameLog table
class BoardGameLog(db.Model, UserMixin):
    log_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    game_id = db.Column(db.Integer, db.ForeignKey('board_game.game_id'))
    rating = db.Column(db.Numeric(2, 1))
    players = db.Column(db.Integer)
    description = db.Column(db.Text)
    image = db.Column(db.String(255))