'''
Created on 18/09/2013

@author: HelderSi
'''
from django.conf.urls import patterns, include, url
from .views import UsuarioCreate
from django.views.generic import TemplateView



urlpatterns = patterns('',
#url(r'^$', UsuarioCreate.as_view()),
    url(r'^thanks/$', TemplateView.as_view(template_name='thanks.html')),
)
