import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(100), nullable=False)
    name = Column(String(20), nullable=False)
    lastname = Column(String(20), nullable=False)
    created = Column(DateTime(timezone=False))

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    caption = Column(String(255))
    image_url = Column(String(255))
    created = Column(DateTime(timezone=False))
    #user_id=Column(Integer, ForeignKey=('user.id'))
    #user = relationship('User')

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    caption = Column(String(255))
    created = Column(DateTime(timezone=False))
    #user_id = Column(Integer, ForeignKey('user.id'))
    #post_id=Column(Integer, ForeignKey=('post.id'))
    #user = relationship('User')
    #post = relationship('Post')

class Like(Base):
    __tablename__='like'
    id=Column(Integer, primary_key=True)
    #user_id=Column(Integer, ForeignKey=('user.id'))
    #post_id=Column(Integer, ForeignKey=('post.id'))
   # user = relationship('User')
    #post = relationship('Post')


class Follower(Base):
    __tablename__='follower'
    id=Column(Integer, primary_key=True)
    name=Column(String(100), nullable=False) 
    #user_id=Column(Integer, ForeignKey=('user.id'))

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
