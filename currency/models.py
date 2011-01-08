from django.db import models
from django.utils.encoding import smart_unicode
import managers

class Currency(models.Model):
    code = models.CharField(max_length=20, primary_key=True)
    symbol = models.CharField(max_length=10)
    positive_format = models.CharField(max_length=40)
    negative_format = models.CharField(max_length=40)
    decimal_symbol = models.CharField(max_length=5, default='.')
    decimal_places = models.PositiveSmallIntegerField(default=0)
    group_symbol = models.CharField(max_length=5, default=',')
    group = models.BooleanField(default=True)
    
    objects = managers.CurrencyManager()
    
    def __unicode__(self):
        return u'Currency(%s %s)' % (self.code, smart_unicode(self.symbol))
        
    def toDict(self):
        return dict([(field, getattr(self, field))for field in self.__class__._meta.get_all_field_names()])
