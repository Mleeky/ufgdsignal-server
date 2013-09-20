'''
Created on 18/09/2013

@author: HelderSi
'''

from django.contrib import admin
from .models import *

admin.site.register(AnuncianteProfile)
admin.site.register(AdminProfile)
admin.site.register(ConfigProfile)