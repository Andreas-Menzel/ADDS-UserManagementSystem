import functools

from flask import (
    Blueprint, flash, g, jsonify, redirect, render_template, request, session, url_for
)

from flaskr.db import get_db

from backports.pbkdf2 import pbkdf2_hmac
from datetime import datetime
import time
import jwt


# Import own files
from collection import *


bp = Blueprint('account', __name__, url_prefix='/account')


@bp.route('/create')
def create_account():
    response = get_response_template()

    # Get parameter
    email = request.values.get('email')
    firstname = request.values.get('firstname')
    lastname = request.values.get('lastname')
    pwd_salt = request.values.get('pwd_salt')
    pwd_hash = request.values.get('pwd_hash')

    # Check if required parameter was given
    response = check_argument_not_null(response, email, "email")
    response = check_argument_not_null(response, firstname, "firstname")
    response = check_argument_not_null(response, lastname, "lastname")
    response = check_argument_not_null(response, pwd_salt, "pwd_salt")
    response = check_argument_not_null(response, pwd_hash, "pwd_hash")

    # Return if an error already occured
    if not response['executed']:
        return jsonify(response)

    db = get_db()

    # Check if user with given email already exists
    db_user_info = db.execute(
        'SELECT * FROM users WHERE email = ?', (email,)).fetchone()
    if not db_user_info is None:
        response = add_error_to_response(
            response,
            1,
            f'User with email "{email}" already exists You can delete your account without password if you haven\'t activated it yet.',
            False
        )

    # Return if an error already occured
    if not response['executed']:
        return jsonify(response)

    created = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    activation_code = generate_activation_code()

    db.execute("""INSERT INTO users(email, firstname, lastname, pwd_salt, pwd_hash, created, activation_code)
                  VALUES(?, ?, ?, ?, ?, ?, ?)""", (email, firstname, lastname, pwd_salt, pwd_hash, created, activation_code,))
    db.commit()

    # TODO: send email
    send_account_activation_mail(email, firstname, lastname, created, activation_code)

    return jsonify(response)


@bp.route('/activate')
def activate_account():
    response = get_response_template()

    # Get parameter
    activation_code = request.values.get('activation_code')

    # Check if required parameter was given
    response = check_argument_not_null(
        response, activation_code, "activation_code")
    
    activation_code = activation_code.upper()

    # Return if an error already occured
    if not response['executed']:
        return jsonify(response)

    db = get_db()

    # Check if user with given activation code exists
    db_user_info = db.execute(
        """SELECT * FROM users
           WHERE activation_code = ?""", (activation_code,)).fetchone()
    if db_user_info is None:
        response = add_error_to_response(
            response,
            1,
            f'The activation code "{activation_code}" is not valid.',
            False
        )

    # Return if an error already occured
    if not response['executed']:
        return jsonify(response)

    activation_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    db.execute("""UPDATE users
                  SET activation_time = ?,
                      activation_code = ?""", (activation_time, None,))
    db.commit()

    return jsonify(response)
