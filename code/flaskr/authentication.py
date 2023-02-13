import functools

from flask import (
    Blueprint, flash, g, jsonify, redirect, render_template, request, session, url_for
)

from flaskr.db import get_db

from backports.pbkdf2 import pbkdf2_hmac
import time
import jwt


# Import own files
from collection import *


bp = Blueprint('authentication', __name__, url_prefix='/authentication')


# Request authentication.
# This does not authenticate yet. This returns the password salt for the
# specified user.
@bp.route('/request')
def request_authentication():
    response = get_response_template(payload=True)

    # Get parameter
    email = request.values.get('email')

    # Check if required parameter was given
    response = check_argument_not_null(response, email, "email")

    # Return if an error already occured
    if not response['executed']:
        return jsonify(response)

    db = get_db()

    # Check if active drone with given id exists
    db_user_info = db.execute(
        'SELECT * FROM users WHERE email = ?', (email,)).fetchone()
    if db_user_info is None:
        response = add_error_to_response(
            response,
            1,
            f'No user with email "{email}" found.',
            False
        )

    # Return if an error already occured
    if not response['executed']:
        return jsonify(response)

    response['payload']['email'] = email
    response['payload']['salt'] = db_user_info['pwd_salt']

    return jsonify(response)


# Authenticate.
@bp.route('/authenticate')
def authenticate():
    response = get_response_template(payload=True)

    # Get parameter
    email = request.values.get('email')
    pwd_hash = request.values.get('pwd_hash')

    # Check if required parameter was given
    response = check_argument_not_null(response, email, "email")
    response = check_argument_not_null(response, pwd_hash, "pwd_hash")

    # Return if an error already occured
    if not response['executed']:
        return jsonify(response)

    db = get_db()

    # Check if active drone with given id exists
    db_user_info = db.execute(
        'SELECT * FROM users WHERE email = ?', (email,)).fetchone()
    if db_user_info is None:
        response = add_error_to_response(
            response,
            1,
            f'No user with email "{email}" found.',
            False
        )

    # Return if an error already occured
    if not response['executed']:
        return jsonify(response)

    if not pwd_hash == db_user_info['pwd_hash']:
        response = add_error_to_response(
            response,
            1,
            f'The given password hash is not valid for the user with the email "{email}". Hash is "{db_user_info["pwd_hash"]}"',
            False)

    # Return if an error already occured
    if not response['executed']:
        return jsonify(response)

    response['payload']['email'] = email
    expire = round(time.time()) + 60  # The token is valid for 1 minute
    response['payload']['exp'] = expire

    auth_token = jwt.encode(
        response['payload'], private_key, algorithm="RS256")

    response['payload']['auth_token'] = auth_token

    return jsonify(response)
