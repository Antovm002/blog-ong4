from .settings import *

"""conexion = mysql.connector.connect(user='', password='Antito48962620',host='localhost',database='blogong4',port='3306')"""
SETTINGFILES_DIRS = {
    os.path.join(os.path.dirname(BASE_DIR), "/calendarapp/eventcalendar/settings"),
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'blogong4',
        'USER': 'root',
        'PASSWORD': 'Juliasuse@1997',
        'HOST': 'localhost',
        'PORT': '3306',
}
}