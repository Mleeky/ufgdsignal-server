'''
Created on 19/09/2013

@author: HelderSi
'''

from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'index.html'    