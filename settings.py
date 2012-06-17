APP_KEY    = "KEY"
APP_SECRET = "SECRET"

try:
    from local_settings import *
except Exception, err:
    pass