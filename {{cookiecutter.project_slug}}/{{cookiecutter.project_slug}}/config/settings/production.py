import os
from .base import settings

settings['DATABASES'] = {
    'default': {
        'ENGINE': 'mssql+pymssql',
        'HOST': os.getenv('DEFAULT_HOST'),
        'NAME': os.getenv('DEFAULT_NAME'),
        'USER': os.getenv('DEFAULT_USER'),
        'PASSWORD': os.getenv('DEFAULT_PASSWORD'),
        'PORT': os.getenv('DEFAULT_PORT')
    }
}
