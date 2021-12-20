"""
django-guardian is an implementation of object permissions
for Django providing an extra authentication backend.

https://django-guardian.readthedocs.io/en/stable/

Configuration:

    AUTHENTICATION_BACKENDS = (
        'django.contrib.auth.backends.ModelBackend',
        'guardian.backends.ObjectPermissionBackend',
    )

Optional settings:

    GUARDIAN_RENDER_403
    GUARDIAN_TEMPLATE_403
    ANONYMOUS_USER_NAME
    GUARDIAN_GET_INIT_ANONYMOUS_USER
    GUARDIAN_GET_CONTENT_TYPE
    GUARDIAN_AUTO_PREFETCH
    GUARDIAN_USER_OBJ_PERMS_MODEL

"""
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'guardian.backends.ObjectPermissionBackend',
)
