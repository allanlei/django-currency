import base

class Backend(base.Backend):
    def __init__(self, *args, **kwargs):
        print 'LOCMEM INIT'
        from currencies.fixtures.currencies import CURRENCIES
        dict.__init__(self, CURRENCIES)
        
    def __getitem__(self, key):
        return dict.__getitem__(self, key)

    def __setitem__(self, key, value):
        return dict.__setitem__(self, key, value)

    def __delitem__(self, key):
        return dict.__delitem__(self, key)
