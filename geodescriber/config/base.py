import os
from geodescriber.utils.files import BASE_DIR, PROJECT_DIR

SETTINGS = {
    'logging': {
        'level': 'DEBUG'
    },
    'service': {
        'port': 4501
    },
    'gee': {
        'service_account': 'earth-engine@notional-impact-169016.iam.gserviceaccount.com',
        'privatekey_file': BASE_DIR + '/privatekey.json',
        'assets': {
            'geodescriber':'projects/wri-datalab/geodesriber-asset-v2'
        },
    },
    'redis': {
        'url': os.getenv('REDIS_URL')
    }
}
