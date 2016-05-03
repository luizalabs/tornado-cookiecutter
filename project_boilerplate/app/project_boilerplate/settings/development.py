from .base import settings

settings['DATABASES'] = {
    'default': {
        'ENGINE': 'mssql+pymssql',
        'HOST': 's500devsql01.magazineluiza.intranet',
        'NAME': 'dbmagazine_xp',
        'USER': 'devfcamara',
        'PASSWORD': 'DEVFCAMARA',
        'PORT': 1433
    }
}

