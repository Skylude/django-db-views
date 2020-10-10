from __future__ import unicode_literals


DATABASES = {
    "default": {},
    "sqllite": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:"
    },
    "postgres": {
        'ENGINE': 'django.db.backends.postgresql',
        "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "127.0.0.1",
        "PORT": "5022",
    }
}


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django_db_views.tests.testapp.apps.TestAppConfig",
    "django_db_views"
]

SITE_ID = 1

SECRET_KEY = "test"
