# Sending email
# https://docs.djangoproject.com/en/{{ docs_version }}/topics/email/

EMAIL_BACKEND = config('EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')

EMAIL_HOST = config('EMAIL_HOST', default='')

EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')

EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')

EMAIL_PORT = config('EMAIL_PORT', default='')

EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=True, cast=bool)

DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL', default='')