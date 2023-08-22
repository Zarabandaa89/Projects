import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SQLITE = {
    'default': {
        'ENGINE': 'djan.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR,'db.sqlite3')
    }
}

MYSQL = {
    'default':{
        'ENGINE':'django.db.backends.mysql',
        'NAME': 'dbprueba4',
        'USER': 'root',
        'PASSWORD': '1019604589Sz.',
        'HOST': 'localhost',
        'PORT': '3306'
        
    }
}