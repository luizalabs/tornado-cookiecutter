from .base import settings

settings['DATABASES'] = {
    'default': 'mssql+pymssql://devfcamara:DEVFCAMARA@s500sqldev01.magazineluiza.intranet:1433/'
}
