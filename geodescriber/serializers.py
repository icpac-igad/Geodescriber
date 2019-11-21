"""Serializers"""
import logging


def serialize_geodescriber(analysis, type):
    """Serialize response"""
    return {
        'id': None,
        'type': type,
        'attributes': {**analysis}
    }