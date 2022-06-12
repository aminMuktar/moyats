from . import models
from django.contrib import admin
from django.contrib.auth.models import Group
from core.models import BaseContact

admin.site.unregister(Group)
admin.site.register(BaseContact)
admin.site.register(models.Address)
admin.site.register(models.NotificationSetting)
admin.site.register(models.BaseUser)
admin.site.register(models.EmailVerificationCode)
admin.site.register(models.UserPayment)