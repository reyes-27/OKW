from .base import *
from .third_party import *
from .celery_settings import *
if DEBUG:
    from .local import *
else:
    from .prod import *
