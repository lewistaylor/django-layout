import socket
import sys

#### DEFAULT VALUES ####

CONTEXT = ''  # Example: http://www.example.com/django -> /django


#### SERVER CONFIG ####

PRODUCTION_SERVERS = (
                'dangerfarms.com',
                )


STAGING_SERVERS = (
                   )
                   
                   
DEVELOPMENT_SERVERS = (
                       )


if socket.gethostname() in PRODUCTION_SERVERS:
    from project.settings.production import *
elif socket.gethostname() in STAGING_SERVERS:
    from project.settings.staging import *
elif socket.gethostname() in DEVELOPMENT_SERVERS:
    from project.settings.development import *
elif 'runserver' in sys.argv:
    from project.settings.local import *
elif 'test' in sys.argv or [arg for arg in sys.argv if 'nosetests' in arg]:
    from project.settings.test import *
else:
    from project.settings.production import *
    
    
    
#### MEDIA & URL RESOLVING ####

MEDIA_URL = '%s/media/' % CONTEXT
STATIC_URL = '%s/static/' % CONTEXT

LOGIN_URL = '%s/login/' % CONTEXT
LOGOUT_URL = '%s/logout/' % CONTEXT
LOGIN_REDIRECT = '%s/' % CONTEXT


#### OPTIMIZATION ####

MIDDLEWARE_CLASSES = tuple(MIDDLEWARE_CLASSES)
INSTALLED_APPS = tuple(INSTALLED_APPS)
