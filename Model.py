from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Date, Integer, String


ma = Marshmallow()
db = SQLAlchemy()

class Binome(db.Model):

    __tablename__ = 'Binomes'

    massar1 = Column(String(30),primary_key = True)
    nom1 = Column(String(30), nullable=False)
    prenom1 = Column(String(30), nullable=False)
    nom2 = Column(String(30),nullable = True)
    prenom2 = Column(String(30),nullable = True)
    massar2 = Column(String(30), unique=True, nullable=True)
    password = Column(String(50), nullable=False)
    filiere = Column(String(4), nullable=False)
    hasPFE = Column(Integer,nullable = False, default = 0)
    def __init__(self,massar1,nom1,prenom1,nom2,prenom2,massar2,password,filiere,hasPFE):
        self.filiere = filiere
        self.massar1 = massar1
        self.massar2 = massar2
        self.nom1 = nom1
        self.nom2 = nom2
        self.prenom2 = prenom2
        self.prenom1 = prenom1
        self.password = password
        self.hasPFE = hasPFE

    def __repr__(self):
        return '<User {}>'.format(self.nom1)
    def serialize(self):
        return {
            'massar1' : self.massar1,
            'massar2' : self.massar2,
            'nom1' : self.nom1,
            'nom2' : self.nom2,
            'prenom1' : self.prenom1,
            'prenom2' : self.prenom2,
            'filiere' : self.filiere,
            'password' : self.password,
            'hasPFE' : self.hasPFE
        }

class BinomeSchema(ma.Schema):
    class Meta:
        fields=('massar1','massar2','nom1','nom2','prenom1','prenom2','filiere','password','hasPFE')


class Binome_Schema(ma.Schema):
    class Meta:
        fields=('massar1','nom1','prenom1','filiere','password','hasPFE')


binomesch= Binome_Schema(strict=True)

binome_schema = BinomeSchema(strict=True)
binomes_schema = BinomeSchema(many=True,strict=True)
class pfe(db.Model):
    __tablename__ = 'PFE'

    id = Column(Integer,primary_key=True)
    Filiere = Column(String(4),nullable=False)
    titre = Column(String(100),nullable = False,unique=True)
    taken = Column(Integer,default = 0,nullable=False)
    description = Column(String(500),nullable = False)
    profid = Column(Integer , db.ForeignKey('Professeur.id', ondelete='CASCADE'),nullable=False)
    prof = db.relationship('Professeur', backref=db.backref('PFE',lazy = 'dynamic'))
    def serialize(self):
        return {
            'id' : self.id,
            'Filiere' : self.Filiere,
            'taken' : self.taken,
            'description' : self.description,
        }
    def __init__(self,Filiere,titre,description,profid):
        self.profid = profid
        self.Filiere = Filiere
        self.description = description
        self.titre = titre



class Professeurs(db.Model):
    __tablename__ = 'Professeurs'
    id = Column(Integer,primary_key=True)
    Filiere = Column(String(4),nullable=False)
    Nomprof = Column(String(30),nullable = False)
    Prenomprof = Column(String(30),nullable = False)
    email = Column(String(50),nullable = False)
    def __init__(self, Filiere,Nomprof,Prenomprof,email):
        self.Filiere = Filiere
        self.Nomprof = Nomprof
        self.Prenomprof = Prenomprof
        self.email = email
    
class ProfesseurSchema(ma.Schema):
    class Meta : 
        id = fields.Integer()
        Nomprof = fields.String(required=True)
        Prenomrof = fields.String(required=True)
        email = fields.String(required=True)
        Filiere = fields.String(required=True)

class PFEschema(ma.Schema):
    class Meta:
        id = fields.Integer()
        Filiere = fields.String()

    
    
