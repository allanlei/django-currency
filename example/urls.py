from django.conf.urls.defaults import *
from django.views import generic

import views

urlpatterns = patterns('',
    url(r'^$', views.TestView.as_view()),
)
