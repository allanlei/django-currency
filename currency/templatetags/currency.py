from django import template
from django.conf import settings
from .. import utils
from .. import models

register = template.Library()

@register.filter
def currency(value, region=getattr(settings, 'CURRENCY_DEFAULT_REGION', settings.LANGUAGE_CODE)):
    curr = models.Currency.objects.get_currency(region)
    return utils.toCurrency(value, **curr.toDict())
