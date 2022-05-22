from . import models
from django.contrib import admin
from django.contrib.auth.models import Group


admin.site.unregister(Group)
admin.site.register(models.BaseContact)
admin.site.register(models.UserProfile)
admin.site.register(models.Address)
admin.site.register(models.NotificationSetting)
admin.site.register(models.BaseUser)