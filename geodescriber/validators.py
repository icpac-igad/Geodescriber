"""VALIDATORS"""
from flask import request
from functools import wraps
from geodescriber.routes.api import error


def validate_geostore(func):
    """World Validation"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        if request.method == 'GET':
            geostore = request.args.get('geostore')
            if not geostore:
                return error(status=400, detail='Geostore is required')
        return func(*args, **kwargs)
    return wrapper