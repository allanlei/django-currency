import base

from currencies.models import Currency

class Backend(base.Backend):
    def __init__(self, *args, **kwargs):
        print 'DB INIT'
        dict.__init__(self, CURRENCIES)
        
    def __getitem__(self, key):
        try:
            curr = Currency.objects.get(code=key)
            return {
                'symbol': cur.symbol,
		        'positive_format': curr.positive_format,
		        'negative_format': curr.negative_format,
		        'decimal_symbol': curr.decimal_symbol,
		        'digit_group_symbol': curr.digit_group_symbol,
		        'group_digits': curr.group_digits,
            }
        except Currency.DoesNotExist:
            raise KeyError

    def __setitem__(self, key, value):
        Currency.objects.get_or_create(code=key, **value)

    def __delitem__(self, key):
        return Currency.objects.get(code=key).delete()
