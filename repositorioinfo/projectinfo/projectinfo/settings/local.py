from .settings import *
import mysql.connector

conexion = mysql.connector.connect(user='antonela', password='Antito48962620',host='localhost',database='blogong4',port='3306')
"""SETTINGFILES_DIRS = {
    os.path.join(os.path.dirname(BASE_DIR), "/calendarapp/eventcalendar/settings"),
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'blogong4',
        'USER': 'antitovm',
        'PASSWORD': 'antito48962620',
        'HOST': 'localhost',
        'PORT': '',
}
}"""