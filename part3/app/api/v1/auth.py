from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.services.facade import HBnBFacade
from datetime import timedelta
from http import HTTPStatus

facade = HBnBFacade()
api = Namespace('auth', description='Authentication operations')
api_protected = Namespace('protected', description='Protected operations')


# Modèles pour la validation et la documentation
login_model = api.model('Login', {
    'email': fields.String(required=True, description='User email address',
                         example='user@example.com'),
    'password': fields.String(required=True, description='User password',
                           example='********')
})

token_response = api.model('TokenResponse', {
    'access_token': fields.String(description='JWT access token'),
    'token_type': fields.String(description='Token type', example='bearer'),
    'expires_in': fields.Integer(description='Token expiration time in seconds')
})

error_response = api.model('ErrorResponse', {
    'error': fields.String(description='Error message'),
    'status_code': fields.Integer(description='HTTP status code')
})

@api.route('/login')
class Login(Resource):
    @api.expect(login_model)
    @api.response(200, 'Success', token_response)
    @api.response(401, 'Authentication failed', error_response)
    @api.response(422, 'Validation Error', error_response)
    def post(self):
        """Authenticate user and return a JWT token"""
        credentials = api.payload

        if 'email' not in credentials or 'password' not in credentials:
            return {'error': 'Missing email or password'}, 400
        
        user = facade.get_user_by_email(credentials['email'])
        
        if not user or not user.verify_password(credentials['password']):
            return {'error': 'Invalid credentials'}, 401

        access_token = create_access_token(identity={'id': str(user.id), 'admin': user.admin})
        
        return {'access_token': access_token}, 200


@api.route('/protected')
class ProtectedResource(Resource):
    @jwt_required()
    def get(self):
        """A protected endpoint that requires a valid JWT token"""
        # Récupérer l'identité de l'utilisateur à partir du token JWT
        current_user = get_jwt_identity()

        # Utiliser les informations de l'utilisateur, par exemple :
        user_id = current_user['id']
        is_admin = current_user['admin']

        # Retourner une réponse protégée
        return {'message': f'Hello, user {user_id}!'}, 200
