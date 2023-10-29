from django.contrib import admin
from TaskHive.models import Taskdb

class TaskdbAdmin(admin.ModelAdmin):
    list_display=('title','date','user')

admin.site.register(Taskdb,TaskdbAdmin)

# Register your models here.
