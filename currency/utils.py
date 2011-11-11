## -*- coding: utf-8 -*-
#from django.utils.encoding import smart_unicode
#from fixtures.regions import REGIONS

#from decimal import Decimal
#import math, re


#class CurrencyFormatError(Exception):
#    pass

#ACCEPTED_INPUT_VALUES = (int, long, float)

#def number_separate(value, seperator=','):
#    orig = unicode(value)
#    sub = '\g<1>%s\g<2>' % seperator
#    new = re.sub('^(-?\d+)(\d{3})', sub, orig)
#    if orig == new:
#        return new
#    else:
#        return number_separate(new, seperator)

#def round_decimal(value, decimal_places=2):
#    rounding = Decimal(10) ** (decimal_places * -1)
#    return value.quantize(rounding)


#def toCurrency(value, symbol, code=None, positive_format=None, negative_format=None, decimal_symbol='.', group_symbol=',', group=True, decimal_places=0):
#    if not isinstance(value, ACCEPTED_INPUT_VALUES):
#        raise CurrencyFormatError('Input value needs to be one of %s. Found %s' % (', '.join([str(t.__name__) for t in ACCEPTED_INPUT_VALUES]), value.__class__.__name__))
#    if value >= 0 and positive_format is None:
#        raise CurrencyFormatError('Positive format required')
#    if value < 0 and negative_format is None:
#        raise CurrencyFormatError('Negative format required')
#    
#    format = positive_format if value >= 0 else negative_format
#    symbol = smart_unicode(symbol)
#    
#    value = math.fabs(value)
#    if isinstance(value, float):
#        value = Decimal(unicode(value))
#    value = round_decimal(Decimal(value), decimal_places)
#    
#    split = smart_unicode(value).split('.')
#    integer = split[0]
#    decimals = split[1] if len(split) == 2 else ''
#        
#    format_args = {
#        'symbol': symbol,
#        'amount': '%s%s' % (
#            number_separate(int(integer), smart_unicode(group_symbol)) if group else integer, 
#            '%s%s' % (decimal_symbol, decimals) if decimal_places > 0 else ''
#        )
#    }
#    return format % format_args

#def fromCurrency(value):
#    return value
