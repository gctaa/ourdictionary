import os
DJANGO_ENVIRONMENT = os.environ.get('DJANGO_ENVIRONMENT', 'dev') 
exec('from settings_%s import *' % DJANGO_ENVIRONMENT)
