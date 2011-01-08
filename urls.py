from django.conf.urls.defaults import *

urlpatterns = patterns('',
     (r'^django_currency/', include('django_currency.currency.urls')),
)
