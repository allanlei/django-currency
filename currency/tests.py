"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from currency.models import Currency
from currency.fixtures.regions import REGIONS

class SimpleTest(TestCase):
    def test_currency_fixture(self):
        for region in REGIONS:
            print region, Currency.objects.get_currency_fixture(region)
    
    def test_currency_ajax(self):
        for region in REGIONS:
            print region, Currency.objects.get_currency_ajax(region)
            
    def test_currency_db(self):
        for region in REGIONS:
            print region, Currency.objects.get_currency_db(region)
