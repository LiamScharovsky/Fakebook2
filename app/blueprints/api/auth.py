from flask_httpauth import HTTPBasicAuth
from app.blueprints.blog.models import User

basic_auth = HTTPBasicAuth()

@basic_auth.verifyPassword
def verifyPassword(email, password):
    user = User.query.filter_by(email=email).first()
    if user and user.checkPassword(password):
        return User     