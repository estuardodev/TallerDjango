from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent # Ruta base que utilizará Django

# Clave de seguridad que usara Django para el cifrado y decifrado 
# Esta clave debe de ser privada, aconsejo utilizar .env
SECRET_KEY = 'xyxvpkf*!oz!olrgv9gc@#0(k4(s^-omu&qw!=qufx@o_c761o548484rrewfhryjh'

# Con esto veremos los problemas que tenga nuestro sitio web si en dado caso tiene
# En producción siempre debe de ser False
DEBUG = True

ALLOWED_HOSTS = [] # Son los dominios que acepta nuestro sitio


# Application definition

# Acá indicamos cuales son las aplicaciones nuestras y de terceros que utilizaremos
# Consejo, evitar colocar otras apps antes de las de django
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Apps Propias
    'App1.apps.App1Config',
    'mi_api',

    # Aplicaciones de Terceros
    'rest_framework',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Taller.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Taller.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
# Acá indicamos que base de datos utilzaremos
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'es-us' # Idioma que manejará django
# https://es.wikipedia.org/wiki/ISO_639-1

TIME_ZONE = 'UTC' # Zona horaria que manejará django
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/' # Como se identificará la ruta de los archivos estáticos
# En producción utilizaremos esto:
# import os
# STATIC_ROOT = os.path.join(BASE_DIR, "static/")

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configuración de Rest Framework

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}