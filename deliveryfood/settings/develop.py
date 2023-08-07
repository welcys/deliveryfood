from .base import *
AUTH_USER_MODEL = "user.User"
DEBUG = True

DATABASES = {
    'default': {'ENGINE': 'django.db.backends.mysql',
                'NAME': 'deliveryfood',
                'USER': 'root',
                'PASSWORD': 'Asdf1234.',
                'HOST': '127.0.0.1',
                'PORT': '3306',
                }
}

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'PARSER_CLASS': 'redis.connection.HiredisParser',
        },
    },
}


