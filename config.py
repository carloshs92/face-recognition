import logging
import os


class BaseConfig(object):
    """Base class for default set of configs."""
    DEBUG = False
    TESTING = False
    SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
    SECURITY_TRACKABLE = True
    LOGGING_FORMAT = "[%(asctime)s] [%(funcName)-30s] +\
                                    [%(levelname)-6s] %(message)s"
    LOGGING_LOCATION = 'web.log'
    LOGGING_LEVEL = logging.DEBUG
    SECURITY_TOKEN_MAX_AGE = 60 * 30
    SECURITY_CONFIRMABLE = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CACHE_TYPE = 'simple'
    SECURITY_PASSWORD_SALT = 'super-secret-stuff-here'
    COMPRESS_MIMETYPES = ['text/html', 'text/css', 'text/xml',
                          'application/json', 'application/javascript']
    WTF_CSRF_ENABLED = False
    COMPRESS_LEVEL = 6
    COMPRESS_MIN_SIZE = 500


class DevelopmentConfig(BaseConfig):
    """Default set of configurations for development mode."""
    DEBUG = True
    TESTING = False
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    SECRET_KEY = u'not-so-super-secret'