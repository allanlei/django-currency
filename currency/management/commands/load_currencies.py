# -*- coding: utf-8 -*-
from optparse import make_option

from django.conf import settings
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    option_list = loaddata.Command.option_list + (
#        make_option('--schema', action='store', dest='schema', default=None, help='HELP TEXT'),
    )
    help = 'HELP TEXT'
    
    def handle(self, *args, **options):
        pass
