import os
import psycopg2
import dj_database_url


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'f&$m36vh_t(l_)aeg)y5dhed2=db)02wtrl_(p7^@85-+wr^22'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "localhost", "localhost:8000", "0.0.0.0", "almamater0.herokuapp.com"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'principal',
    'almamater0',

    'spirit.core',
    'spirit.admin',
    'spirit.search',

    'spirit.user',
    'spirit.user.admin',
    'spirit.user.auth',

    'spirit.category',
    'spirit.category.admin',

    'spirit.topic',
    'spirit.topic.admin',
    'spirit.topic.favorite',
    'spirit.topic.moderate',
    'spirit.topic.notification',
    'spirit.topic.private',
    'spirit.topic.unread',

    'spirit.comment',
    'spirit.comment.bookmark',
    'spirit.comment.flag',
    'spirit.comment.flag.admin',
    'spirit.comment.history',
    'spirit.comment.like',
    'spirit.comment.poll',

    'djconfig',
    'haystack',
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'spirit.user.middleware.TimezoneMiddleware',
    'spirit.user.middleware.LastIPMiddleware',
    'spirit.user.middleware.LastSeenMiddleware',
    'spirit.user.middleware.ActiveUserMiddleware',
    'spirit.core.middleware.PrivateForumMiddleware',
    'djconfig.middleware.DjConfigMiddleware',
]

ROOT_URLCONF = 'almamater0.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'almamater0.wsgi.application'

DATABASE_URL='postgres://quxyteosyveldg:2e64257288a1e29c8dfde0a5a8225a596ca39d52fa714591cb4effe8f04ed50e@ec2-54-247-98-162.eu-west-1.compute.amazonaws.com:5432/da2rcv7d0eof0a'

conn = psycopg2.connect(DATABASE_URL, sslmode='require')
DATABASES = {'default': dj_database_url.config(default=DATABASE_URL)}

#DATABASES = {
    #'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    #}
#}

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(BASE_DIR, 'st_search'),
    },
}

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us' #quizsa cambiar esto para los avisos en ingles

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_URL='/user/login/'
LOGIN_REDIRECT_URL='/path/to/redirecturl'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATIC_ROOT = os.path.join(BASE_DIR, "static")

STATICFILES_DIR=(
    os.path.join(BASE_DIR, 'static'),
)

#esto es de spirit

#: The category's PK containing all of the private topics.
#: The category is auto-created and so this value should not change
ST_TOPIC_PRIVATE_CATEGORY_PK = 1

#: Enable/disable the rate-limit for all forms
ST_RATELIMIT_ENABLE = True
#: The cache key prefix. This is mostly to avoid clashing with other apps
ST_RATELIMIT_CACHE_PREFIX = 'srl'
#: The cache ID for storing rate-limit related data.
#: The cache ID must be a valid ``CACHES`` entry and
#: the ``TIMEOUT`` must be ``None`` otherwise it will misbehave
ST_RATELIMIT_CACHE = 'st_rate_limit' #ponia 'st_rate_limit"
#: A warning will be printed when the ``TIMEOUT``
#: is not ``None``. Setting this to ``True`` will silence it.
#:
#: .. Warning:: A ``ConfigurationError`` will be raised instead of a warning in Spirit > 0.5
ST_RATELIMIT_SKIP_TIMEOUT_CHECK = False

#: Number of notifications per page
ST_NOTIFICATIONS_PER_PAGE = 20

#: Maximum length for a comment
ST_COMMENT_MAX_LEN = 3000
#: Maximum number of mentions per comment willing to process
ST_MENTIONS_PER_COMMENT = 30
#: Minutes to wait before a given user
#: will be able to post a duplicated comment/topic
ST_DOUBLE_POST_THRESHOLD_MINUTES = 30

#: Number of next/previous pages the paginator will show
ST_YT_PAGINATOR_PAGE_RANGE = 3

#: Minimum length for a given search query
ST_SEARCH_QUERY_MIN_LEN = 3

#: Threshold in minutes before the user
#: `"last seen"` info can be updated
ST_USER_LAST_SEEN_THRESHOLD_MINUTES = 1

#: Settings this to ``True`` will require
#: all users to be logged-in to access any section
ST_PRIVATE_FORUM = False

#: Enable/disable image uploads within posts
ST_UPLOAD_IMAGE_ENABLED = True
#: Uploaded images will be validated against these formats.
#: Also, the file choosing dialog will filter by these extensions.
#: See the `Pillow docs <http://pillow.readthedocs.io/en/latest/handbook/image-file-formats.html>`_
#: for a list of supported formats
#:
#: .. Warning::
#:     Allowing PNG files is a security risk as it may contain malicious HTML.
#:     See `Django notes <https://docs.djangoproject.com/en/1.11/topics/security/#user-uploaded-content>`_
ST_ALLOWED_UPLOAD_IMAGE_FORMAT = ('jpeg', 'jpg', 'gif')

#: Enable/disable file uploads within posts.
#: Requires running ``pip install django-spirit[files]`` to install
#: `python-magic <https://github.com/ahupp/python-magic#installation>`_
ST_UPLOAD_FILE_ENABLED = False
#: Uploaded files will be validated against these formats.
#: This is a map of extension and media-type. Both are used for validation
#:
#: .. Note::
#:     To find a media-type just add an extension and an empty media-type,
#:     then try uploading a valid file for that extension and the expected
#:     media-type will be printed within the validation error.
#:     Either that or use the Linux ``file --mime-type ./my_file`` command
ST_ALLOWED_UPLOAD_FILE_MEDIA_TYPE = {
    'doc': 'application/msword',
    'docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    'pdf': 'application/pdf'}

#: Link protocols allowed within posts
ST_ALLOWED_URL_PROTOCOLS = {
    'http', 'https', 'mailto', 'ftp', 'ftps',
    'git', 'svn', 'magnet', 'irc', 'ircs'}

#: Support unicode slugs. Set to ``False``
#: to only allow ASCII chars
ST_UNICODE_SLUGS = True

#: Reject duplicated emails when creating a new account
ST_UNIQUE_EMAILS = True
#: Make emails case insensitive
ST_CASE_INSENSITIVE_EMAILS = True

#: Make user-names case insensitive
#:
#: .. Note::
#:     This can be set to ``False`` at any time,
#:     however setting it back to ``True`` requires
#:     taking care of clashing users,
#:     i.e: ``someuser``, ``SomeUser`` and ``SoMeUsEr``,
#:     only one of those users will be able log-in
#:     (the one in lowercase). Removing clashing users
#:     is usually not possible.
ST_CASE_INSENSITIVE_USERNAMES = True

# Tests helper
ST_TESTS_RATELIMIT_NEVER_EXPIRE = False

# Full route to the spirit package
ST_BASE_DIR = (
    os.path.dirname(
        os.path.dirname(
            os.path.dirname(__file__))))

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'spirit_cache',
    },
    'st_rate_limit': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'spirit_rl_cache',
        'TIMEOUT': None
    }
}

AUTHENTICATION_BACKENDS = [
    'spirit.user.auth.backends.UsernameAuthBackend',
    'spirit.user.auth.backends.EmailAuthBackend',
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false'],
        },
        'console': {
            'class': 'logging.StreamHandler',
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'django.log'),
        },
    },
    'loggers': {
        '': {
            'handlers': ['console', 'mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django': {
            'handlers': ['console', 'mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'celery': {
            'handlers': ['console', 'mail_admins'],
            'level': 'ERROR',
            'propagate': False
        },
    }
}

EMAIL_TIMEOUT = 20
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' #!!!dev

gettext_noop = lambda s: s
LANGUAGES = [
    ('de', gettext_noop('German')),
    ('en', gettext_noop('English')),
    ('es', gettext_noop('Spanish')),
    ('fr', gettext_noop('French')),
    ('hu', gettext_noop('Hungarian')),
    ('it', gettext_noop('Italian')),
    ('lt', gettext_noop('Lithuanian')),
    ('pl', gettext_noop('Polish')),
    ('pl-pl', gettext_noop('Poland Polish')),
    ('ru', gettext_noop('Russian')),
    ('sv', gettext_noop('Swedish')),
    ('tr', gettext_noop('Turkish')),
    ('zh-hans', gettext_noop('Simplified Chinese')),
]