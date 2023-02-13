# This file holds variables and functions that can / will be used by all modules

# These are just demo-keys. Make sure to replace them with the correct keys!
public_key = b"""-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAkyfnPMMVGs6cWvXxbyOY
33Z6RDGePRiPwXQm+Lp87GWrdSOHDcoZHlRJ6URWpEYDGJBukZ/JA416u9IJVbrP
SEYTvSG8wMKFUF8YN/S47yJwaWcfAj06N3w8WBrtjRiM7ofo7elwDGpcKtNDAjlJ
6G9LYLjjb76Mgus6WF2RNClkmAVrCFSFhpBc5otsZDR0c65NacLSbUPXbIhHuMrJ
DhSTn1Sdf0Av5tdcGtUXzaENuwPy95aSp+Yjfjk0RjQDCQ0mSQ6XJ/QSPD388jkD
hpVkLtdwXo90c3yIqCGHdh68MY64jXkfDddRWZEWqgS/VquVznWcfQKUPwt4AhuL
M6hGB5+zK2TWipQV8Zl7xOwiUj4gNDLs5S5Z3knE7aZjdvKtBK3YkPMfYSTu+sMD
w1wpCQsfe+RxUz+RLsj1GyjQ3BUZ0xp2AZ9BznUvlkfCL9N3+HMd0o3jzrC0HJKw
hJO2ENowkSSg+Fj941Frm0mQ0kqWf7LyXzcW5KIrXkAiakl6rm3xCGJA7ZxjbLzR
3Q/ykDU0uCYGa20bdmgGsgJs8JM9+U4lzOkwhiO4zURqmcRQbCIwTpY7XCjDC7IU
UcXzyGM/S0ZCQanmke/4h99KmBi6ht1IC43X6k2HuHZMz0o1V2zmGdzeu9eB9ObT
zAZTBEvoh55H5kUiCBb08BsCAwEAAQ==
-----END PUBLIC KEY-----"""
private_key = b"""-----BEGIN RSA PRIVATE KEY-----
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
-----END RSA PRIVATE KEY-----"""


import random
from string import ascii_uppercase, digits


def generate_random_string(length):
    letters = ascii_uppercase + digits
    return ''.join(random.choice(letters) for i in range(length))


def generate_activation_code():
    return generate_random_string(4) + '-' + generate_random_string(4) + '-' + generate_random_string(4) + '-' + generate_random_string(4)

# Function copied from "https://github.com/python/cpython/blob/b2076b00710c4366dcfe6cd236e480d68a3c38b7/Lib/distutils/util.py#L308"
def strtobool(val):
    """Convert a string representation of truth to true (1) or false (0).
    True values are 'y', 'yes', 't', 'true', 'on', and '1'; false values
    are 'n', 'no', 'f', 'false', 'off', and '0'.  Raises ValueError if
    'val' is anything else.
    """
    val = val.lower()
    if val in ('y', 'yes', 't', 'true', 'on', '1'):
        return 1
    elif val in ('n', 'no', 'f', 'false', 'off', '0'):
        return 0
    else:
        raise ValueError("invalid truth value %r" % (val,))


def get_response_template(payload=False):
    response = {
        'executed': True,
        'errors': [],
        'warnings': []
    }

    if payload:
        response['payload'] = {}

    return response


def add_error_to_response(response, err_id, err_msg, executed=False):
    response['executed'] = executed
    error = {
        'err_id': err_id,
        'err_msg': err_msg
    }
    response['errors'].append(error)

    return response


def add_warning_to_response(response, warn_id, warn_msg):
    warning = {
        'warn_id': warn_id,
        'warn_msg': warn_msg
    }
    response['warnings'].append(warning)

    return response


def check_argument_not_null(response, argument, argument_name, err_id=-1):
    if argument is None:
        response = add_error_to_response(
            response,
            err_id,
            f'Argument missing: {argument_name}',
            False
        )

    return response


def check_argument_type(response, argument, argument_name, data_type, err_id=-1):
    try:
        if data_type == 'int':
            argument = int(argument)
        elif data_type == 'float':
            argument = float(argument)
        elif data_type == 'boolean':
            argument = strtobool(argument)
    except:
        argument = None
        response = add_error_to_response(
            response,
            err_id,
            f'Could not convert "{argument_name}" to {data_type}.'
        )

    return response, argument


def send_email(recipient, subject, message):
    with open('email.txt', 'a') as file:
        file.write(f'E-Mail to: {recipient}\n')
        file.write(f'Subject: {subject}\n')
        file.write(f'Message: {message}\n')


def send_account_activation_mail(email, firstname, lastname, created, activation_code):
    subject = 'Welcome onboard!'
    
    message = ''
    message = message + f'Hello {firstname} {lastname}!'
    message = message + f'You have created an account on {created}.'
    message = message + f'Please use this activation code to activate your account: "{activation_code}".'
    
    send_email(email, subject, message)
