"""MIDDLEWARE"""
from flask import request
from functools import wraps
import json
import logging
from geodescriber.errors import GeostoreNotFound
from geodescriber.routes.api import error
from geodescriber.services.area_service import AreaService
from geodescriber.services.geostore_service import GeostoreService


def get_geo_by_hash(func):
    """Get geodata"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        if request.method == 'GET':
            geostore = request.args.get('geostore')
            if not geostore:
                return error(status=400, detail='Geostore is required')
            try:
                geojson, area_ha = GeostoreService.get(geostore)
            except GeostoreNotFound:
                return error(status=404, detail='Geostore not found')
        elif request.method == 'POST':
            geojson = request.get_json().get('geojson', None) if request.get_json() else None
            try:
                area_ha = AreaService.tabulate_area(geojson)
            except Exception as e:
                logging.info(f"[middleware geo hash] Exception")
                return error(status=500, detail=str(e))
        kwargs["geojson"] = geojson
        kwargs["area_ha"] = area_ha
        return func(*args, **kwargs)
    return wrapper


def get_geo_by_geom(func):
    """Get geometry data"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        if request.method == 'GET':
            #logging.info(f'[decorater - geom]: Getting area by GET {request}')
            geojson = request.args.get('geojson')
            if not geojson:
                return error(status=400, detail='geojson is required')
        elif request.method == 'POST':
            geojson = request.get_json().get('geojson', None) if request.get_json() else None
        try:
            area_ha = AreaService.tabulate_area(geojson)
        except Exception as e:
            return error(status=500, detail=str(e))
        kwargs["geojson"] = geojson
        kwargs['area_ha'] = area_ha
        return func(*args, **kwargs)
    return wrapper