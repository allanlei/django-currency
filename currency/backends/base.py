from django.conf import settings


class Backend(dict):
    def __init__(self, *args, **kwargs):
        dict.__init__(self, *args, **kwargs)
        
    def __getitem__(self, key):
        raise NotImplementedError

    def __setitem__(self, key, value):
        raise NotImplementedError

    def __delitem__(self, key):
        raise NotImplementedError
