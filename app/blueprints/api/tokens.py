from .import bp as api
from flask import jsonify
from app import db
from .auth import basic_auth

@api.route('/tokens', methods=['POST'])
@basic_auth.login_required
def getToken():
    token = basic_auth.current_user().getToken()
    db.session.commit()
    return jsonify({'token': token})

