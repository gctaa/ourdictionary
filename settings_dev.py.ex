from base_settings import *

#Fill this in with relevant DB info
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

INSTALLED_APPS = BASE_INSTALLED_APPS

#Writes out sent emails to the console, useful for debugging
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SECRET_KEY = < replace with generated secret key >
