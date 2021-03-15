"""
Defines the Django Admin model pages for this app .

Registers the models that will be available throgh the Djangpo Admin interface.

For more information see:
https://docs.djangoproject.com/en/2.2/ref/contrib/admin/
"""
from django.contrib import admin
from api.models import Token
from api.models import ConfigFile, ConfigScript, EmergencyContact


admin.site.register(Token)
admin.site.register(ConfigFile)
admin.site.register(ConfigScript)
admin.site.register(EmergencyContact)
