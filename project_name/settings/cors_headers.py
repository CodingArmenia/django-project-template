"""
Django Cors Headers

A Django App that adds Cross-Origin Resource
Sharing (CORS) headers to responses.
This allows in-browser requests to
your Django application from other origins.

https://pypi.org/project/django-cors-headers/
"""
from decouple import config, Csv

CORS_ALLOW_ALL_ORIGINS = config('CORS_ALLOW_ALL_ORIGINS', default=False, cast=bool)

if not CORS_ALLOW_ALL_ORIGINS:
    CORS_ALLOWED_ORIGINS = config('CORS_ALLOWED_ORIGINS', default='', cast=Csv())
