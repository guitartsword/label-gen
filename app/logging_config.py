ERROR_LOG_FILENAME = ".errors.log"

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "loggers": {
        "root":  {
            'level': 'INFO',
            'handlers': [
                'console',
            ],
        },
    },
    'formatters': {
        'default': {
            'format': '%(asctime)s.%(msecs)03d %(name)s:%(lineno)d ' '%(levelname)s %(message)s',
            "datefmt": "%Y-%m-%dT%H:%M:%S",
        }
    },
    'handlers': {
        'console': {
            'formatter': 'default',
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout'
        }
    },
}