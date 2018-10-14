from django.contrib import admin

# Register your models here.

from runningsteve.models import Runner, Race

admin.site.register(Runner)
admin.site.register(Race)
