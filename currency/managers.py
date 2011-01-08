from django.db import models
from django.conf import settings
from fixtures.regions import REGIONS
from collections import namedtuple

class CurrencyManager(models.Manager):
    def __init__(self, *args, **kwargs):
        super(CurrencyManager, self).__init__(*args, **kwargs)
        self.regions = {}
        self.backend = getattr(settings, 'CURRENCY_BACKEND', 'fixture')     #fixture, ajax, db
    
    def __create_currency(self, fields={}):
        from models import Currency
        currency = Currency(**fields)
        return currency
    
    def get_currency_db(self, region, append_db=True):
        print 'get from DB'
        try:
            return self.get(code=region)
        except:
            return None

    def get_currency_fixture(self, region, append_db=True):
        print 'get from fixtures'
        if region in REGIONS:
            currency = REGIONS[region]
        else:
            return None
        if append_db:
            curr, created = self.get_query_set().get_or_create(code=region, defaults=currency)
            return curr
        else:
            return self.__create_currency(fields=currency)
        
    def get_currency_ajax(self, region, append_db=True):
        print 'get from ajax'
        return self.get_currency_fixture(region, append_db)

    def get_currency(self, region, cache=True, append_db=True):
        if cache and region in self.regions:
            print 'FROM CACHE!!'
            return self.regions[region]
        else:
            currency = getattr(self, 'get_currency_%s' % self.backend)(region, append_db)
            if cache:
                self.regions[region] = currency
            return currency
