import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-j_89af+30&&4qm*8z9_(^zz8p4-ho8z_m6ylm0s$h!-p@on1_^'

DEBUG = True

ALLOWED_HOSTS = [
    'localhost',          # Для доступа через http://localhost:8000
    '127.0.0.1',          # Для доступа через http://127.0.0.1:8000 (твой текущий случай)
    '158.160.205.161',    # Внешний IP твоего сервера (на будущее)
    'alvitaski.hopto.org',  # Твой домен (на будущее, чтобы сайт работал по красивому адресу)
    'backend',            # Внутреннее имя сервиса в Docker Compose
    'gateway',
    '123.123.123.123',
]


# ИЗМЕНЕНИЕ 1: Говорим Django доверять заголовкам от прокси-сервера (Nginx/Балансировщика)
USE_X_FORWARDED_HOST = True
# Это критически важная настройка! Она говорит Django:
# "Если в заголовке X-Forwarded-Proto пришло 'https', считай соединение безопасным"
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# ИЗМЕНЕНИЕ 2: Список доверенных источников для CSRF-защиты (обязательно для Django 4.0+)
# Без этого при попытке ввести логин и пароль ты получишь ошибку 403 Forbidden.
CSRF_TRUSTED_ORIGINS = [
    'https://alvitaski.hopto.org',
    'http://alvitaski.hopto.org',
    'http://158.160.205.161',
    'http://localhost:8000',
    'http://127.0.0.1:8000',
]

# Application definition

INSTALLED_APPS = [
    'api.apps.ApiConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

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

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': '/data/db.sqlite3',
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB', 'django'),
        'USER': os.getenv('POSTGRES_USER', 'django'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', ''),
        'HOST': os.getenv('DB_HOST', ''),
        'PORT': os.getenv('DB_PORT', 5432)
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
# При планировании архитектуры было решено,
# что статические файлы Django должны быть доступны по адресу /static/
STATIC_URL = '/static/'
# Указываем корневую директорию для сборки статических файлов;
# в контейнере это будет /app/collected_static
STATIC_ROOT = BASE_DIR / 'collected_static'
# Теперь при вызове команды python manage.py collectstatic
# Django будет копировать все статические файлы в директорию collected_static


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000'
]
