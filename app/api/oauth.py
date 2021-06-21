from flask import jsonify

from . import api
from .. import db
from app.api.trello import is_token_valid, oauth_authorize_url
from ..models import User


@api.route('/oauth/authorize/<int:user_id>')
def get_trello_oauth(user_id):
    user = User.query.filter_by(user_id=user_id).first()
    if user:
        if is_token_valid(user.token):
            return jsonify({
                'status': 'connected'
            })
    return jsonify({
        'user_id': user_id,
        'oauth_url': oauth_authorize_url(user_id)
    })


@api.route('/oauth/redirect/<int:user_id>')
def redirect_oauth_token(user_id):
    return f'''  <script type="text/javascript">
                var token = window.location.href.split("token=")[1]; 
                window.location = "/api/v1/oauth/token/" + token + "/" + {user_id};
            </script> '''


@api.route('/oauth/token/<token>/<int:user_id>')
def get_trello_oauth_token(token, user_id):
    new_token = User(user_id=user_id, token=token)
    db.session.add(new_token)
    db.session.commit()
    return jsonify({
        'Status': 'OK',
    })
