from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):

    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message': 'Store with specified name not found'}, 404


    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': f'Store with name {name} allready exists'}, 400

        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message': 'Some error occured during adding store'}, 500

        return store.json(), 201

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete()


class StoreList(Resource):
    def get(self):
        return {'stores' : [store.json() for store in StoreModel.query.all()]}
