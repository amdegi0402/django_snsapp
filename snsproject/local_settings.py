import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEYS = 'django-insecure-d(7!(qm7cs^r-7i!fg#&i4k-h3$ld@618hy^qr^)!j-_^52!iq' #setting.pyからコピーしたsecret_key

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
DEBUG = True

