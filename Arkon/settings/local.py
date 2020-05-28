from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4z$-c1zmag+8)o(7bjibrl)d-7=jv&tjz-vcrrk%+mg&$d5k#-'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


