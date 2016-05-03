from .base import settings

settings['DATABASES'] = {
    'default': 'sqlite://:memory:'
}
