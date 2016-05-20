import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(BASE_DIR)

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = bool(os.getenv('DEBUG', True))

SQL_ECHO = False

DATABASES = {
    'default': {
        'ENGINE': 'sqlite',
        'HOST': os.getenv('DEFAULT_HOST'),
        'NAME': os.getenv('DEFAULT_NAME'),
        'USER': os.getenv('DEFAULT_USER'),
        'PASSWORD': os.getenv('DEFAULT_PASSWORD'),
        'PORT': os.getenv('DEFAULT_PORT')
    }
}

TEMPLATE_ROOT = os.path.join(BASE_DIR, 'templates')

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

DOCS_URL = '/docs/'
DOCS_ROOT = os.path.join(BASE_DIR, 'docs')

SENTRY_DSN = os.getenv('SENTRY_DSN')
