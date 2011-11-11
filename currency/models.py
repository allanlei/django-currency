from django.db import models


class Currency(models.Model):
    code = models.CharField(max_length=20, primary_key=True)
    symbol = models.CharField(max_length=10)
    positive_format = models.CharField(max_length=40)
    negative_format = models.CharField(max_length=40)
    decimal_symbol = models.CharField(max_length=5, default='.')
    digit_group_symbol = models.CharField(max_length=5, default=',')
    group_symbol = models.CharField(max_length=5, default=',')
    group_digits = models.BooleanField(default=True)
