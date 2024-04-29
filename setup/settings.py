import os
from pathlib import Path
import django_heroku

# Configuração da conexão com o Docker Engine
#DOCKER_BASE_URL = 'unix://var/run/docker.sock'  # ou 'tcp://127.0.0.1:2375' para conexão remota
DOCKER_BASE_URL = 'TCP://127.0.0.1:2375' ##para conexão remota
DOCKER_API_VERSION = 'auto'  # para detectar automaticamente a versão da API Docker

# Criar uma instância do cliente Docker
#docker_client = docker.DockerClient(base_url=DOCKER_BASE_URL, version=DOCKER_API_VERSION)


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-li1dd3ijq(uutb#ksg*-u++-xqrs8b_h&r3wobp2^v0snk&wha'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#DEBUG = False

#SECURE_SSL_REDIRECT

ALLOWED_HOSTS = ['*']

ADMIN_URL = 'admin/'  # Defina o URL do painel de administração
LOGIN_URL = '/accounts/login/'
CSRF_COOKIE_SECURE = False  # Defina como True se estiver usando HTTPS

# hello_django/settings.py

#APP_NAME = os.environ.get("FLY_APP_NAME")  # Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',  # Note a vírgula aqui
    'todos',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

CORS_ALLOWED_ORIGINS = [
    'http://localhost',  # Incluído o esquema e a porta, se aplicável
    'https://projbiblioteca2024.fly.dev'
]

CSRF_TRUSTED_ORIGINS = ['https://biblioteca01-3a799f4d44a2.herokuapp.com']

CORS_ALLOW_METHODS = [
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS',
]

CORS_ALLOW_HEADERS = [
    'Accept',
    'Accept-Language',
    'Content-Language',
    'Content-Type',
    'Authorization',
]

ROOT_URLCONF = 'setup.urls'

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

WSGI_APPLICATION = 'setup.wsgi.application'

# Database

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'Cadastro.sqlite3',
    }
}

# Restante do seu arquivo settings.py...


# Configuração do banco de dados para ambiente local (Windows)
if os.name == 'nt':
    DATABASE_PATH = os.path.join(BASE_DIR, 'Cadastro.sqlite3')
# Configuração do banco de dados para ambiente de produção (fly.io)
else:
    DATABASE_PATH = "/mnt/db-prod.db"

# Restante do seu arquivo settings.py...


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

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

# Adicione estas linhas
DATE_FORMAT = 'dd/mm/YYYY'

DATETIME_FORMAT = 'dd/mm/YYYY H:i:s'

USE_I18N = True

USE_L10N = False

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/


# Static files (CSS, JavaScript)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_URL = '/static/'

# Arquivos de Mídia (Imagens)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

SQLITE3_ROOT = os.path.join(BASE_DIR, 'sqlite3')
SQLITE3_URL = "/venv/"

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

django_heroku.settings(locals())
