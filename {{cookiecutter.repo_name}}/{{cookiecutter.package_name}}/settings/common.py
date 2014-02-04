CELERY_BROKER_URL = "redis://localhost:6379/2"
CELERY_RESULT_BACKEND = "redis://localhost:6379/2"

LOGGING = {
    "version": 1,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter':'verbose',
        },
    },
    'formatters':{
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(name)s %(process)d %(thread)d %(message)s'
        },
    },
    'loggers': {
        '':{
            'handlers':['console'],
            'level':'DEBUG',
            'propogate':True
        },
        'sqlalchemy.engine': {
            'handlers': ['console'],
            'level': 'WARN',
            'propogate': True,
        },
    }
}



