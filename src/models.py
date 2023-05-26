import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    edad =  Column(Integer)
    surnname = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(50), nullable=False)
    favorite_pjs = Column(Integer, ForeignKey("fav_persons.id"))
    favorite_planets = Column(Integer, ForeignKey("fav_planets.id"))

class Personajes(Base):
    __tablename__ = 'personajes'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    height = Column(Integer)
    weigth = Column(Integer)
    gender = Column(String)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    diameter = Column(Integer)
    gravity = Column(Integer)
    population = Column(Integer)
    climate = Column(String)


class Fav_personajes(Base):
    __tablename__ = 'fav_personajes'
    id = Column(Integer, primary_key=True)
    favoritos = Column(Integer, ForeignKey("personajes.id"))

class Fav_planets(Base):
    __tablename__ = 'fav_planets'
    id = Column(Integer, primary_key=True)
    favoritos = Column(Integer, ForeignKey("planets.id"))






    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
