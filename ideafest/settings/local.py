DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysq$
        'NAME': 'ideafest',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'vagrant',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.$
        'PORT': '',                      # Set to empty string for default.
    }
}
