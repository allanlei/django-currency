from django import template
from django.conf import settings

from currencies import currencies, DEFAULT_CURRENCY

register = template.Library()
symbol = 'symbol'
positiveFormat = 'positive_format'
negativeFormat = 'negative_format'
decimalSymbol = 'decimal_symbol'
decimalPlaces = 'decimal_places'
digitGroupSymbol = 'group_symbol'
groupDigits = 'group'



def format_currency(amount, currency):
    if amount >= 0:
        format = currency.get('positive_format', '%(symbol)s%(amount)s')
    else:
        format = currency.get('negative_format', '(%(symbol)s%(amount)s)')
        
    return format % {
        'symbol': currency.get('symbol', '$'),
        'amount': amount,
    }

@register.filter
def currency(amount, curr=DEFAULT_CURRENCY):
    return format_currency(amount, currencies[curr])
