from .settings import *

SETTINGFILES_DIRS = {
    os.path.join(os.path.dirname(BASE_DIR), "/calendarapp/eventcalendar/settings"),
}

DATABASES = {
    'default': {
        'ENGINE': 'mysql',
        'NAME':'blogong4',
        'USER': 'antitovm',
        'PASSWORD': 'antito48962620',
        'HOST': 'localhost\SQLEXPRESS',
        'PORT': '',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server'
    }
}
}