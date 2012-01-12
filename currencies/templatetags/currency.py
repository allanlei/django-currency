from django import template

from currencies import CURRENCIES
from currencies.utils import format


register = template.Library()


@register.filter
def currency(amount, iso='USD'):
    options = CURRENCIES.get(iso, {})
    return format(amount, **options)
