from django.conf import settings
from django.utils import importlib


DEFAULT_CURRENCY_BACKEND = 'currencies.backends.locmem.Backend'
DEFAULT_CURRENCY = getattr(settings, 'DEFAULT_CURRENCY', 'USD')

def get_currencies(backend=DEFAULT_CURRENCY_BACKEND, **kwargs):
    mod_path, cls_name = backend.rsplit('.', 1)    
    mod = importlib.import_module(mod_path)
    Backend = getattr(mod, cls_name)
    return Backend(**kwargs)

currencies = get_currencies(getattr(settings, 'DEFAULT_CURRENCY_BACKEND', DEFAULT_CURRENCY_BACKEND))
