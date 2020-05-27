from flask import request
from flask_restful import Resource
from Model import db,Binome,BinomeSchema,Binome_Schema


binome_schema=BinomeSchema()
binomes_schema=BinomeSchema(many=True)
binomesch = Binome_Schema()

class BinomeResource(Resource):
    def get(self):
        binomes = Binome.query.all()
        binomes = binomes_schema.dump(binomes).data
        return {"message": "success","data" : binomes}, 200

    def post(self):
        jsonD = request.get_json(force=True)
        if not jsonD:
            return {'message': 'No input data provided'}, 400
        data, errors = binome_schema.load(jsonD)
        if errors:
            data,errors = binomesch.load(jsonD)
            if errors :
                return errors, 422
        binome=Binome.query.filter_by(massar1=data['massar1']).first()
        if binome:
            return {'message':'binome deja existant'}, 400
        binome=Binome(
            massar1=jsonD['massar1'],
            nom1=jsonD['nom1'],
            prenom1=jsonD['prenom1'],
            nom2=jsonD['nom2'],
            prenom2=jsonD['prenom2'],
            massar2=jsonD['massar2'],
            password=jsonD['password'],
            filiere=jsonD['filiere'],
            hasPFE=jsonD['hasPFE']
        )
        db.session.add(binome)
        db.session.commit()
        result = binome_schema.dump(binome).data
        return { "status": 'success', 'data': result }, 201
    def put(self):
        jsonD=request.get_json(force=True)
        if not jsonD:
            return {'message': 'No input data provided'}, 400
        data,errors = binome_schema.load(jsonD)
        if errors :
            data,errors = binomesch.load(jsonD)
            if errors : 
                return errors , 422
        binome= Binome.query.filter_by(massar1=data['massar1']).first()
        if not binome:
            return {'message' : 'binome non existant'},400
        
        binome.hasPFE = data['hasPFE']
        binome.filiere = data['filiere']
        binome.nom1 = data['nom1']
        #binome.nom2 = data['nom2']
        binome.filiere = data['filiere']
        binome.massar1=data['massar1']
        #binome.massar2 = data['massar2']
        binome.prenom1 = data['prenom1']
        #binome.prenom2 = data['prenom2']
        db.session.commit()
        result = binome_schema.dump(binome).data
        return {'status' : 'success', 'data' : result},204
    # def get(self):
    #     print('FUCK OFF')
    #     jsonD=request.get_json(force=True)
    #     if not jsonD:
    #         return {'message': 'No input data provided'}, 400
    #     data,errors = binome_schema.load(jsonD)
    #     if errors :
    #         data,errors = binomesch.load(jsonD)
    #         if errors : 
    #             return errors , 422
    #     binome= Binome.query.get(jsonD['massar1'])
    #     print(jsonD)

        
    #     if not binome:
    #         return {'message' : 'binome non existant'},400
        
    #     result = binome_schema.dump(binome).data
    #     return {'status' : 'success', 'data' : result},204
        
        



    