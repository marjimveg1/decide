ALLOWED_HOSTS = ["*"]

MODULES = [
    'base',
    'visualizer',
    'voting',
]

APIS = {
    'base': 'http://localhost:8000',
    'visualizer': 'http://localhost:8000',
    'voting': 'http://localhost:8000',
}

BASEURL = 'http://localhost:8000'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
    
}

# number of bits for the key, all auths should use the same number of bits
KEYBITS = 256
