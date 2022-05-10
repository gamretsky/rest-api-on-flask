from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegistry(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type = str,
                        required = True,
                        help = 'Username field cannot be left blank!')
    parser.add_argument('password',
                        type = str,
                        required = True,
                        help = 'Password field cannot be left blank!')
    def post(self):
        data = UserRegistry.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "User allready exists"}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {'message': "User successfully created"}, 201


if __name__ == '__main__':
    UserModel.find_by_username('Bob')