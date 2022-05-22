from . import models
from django.contrib import admin

admin.site.register(models.EmailReport)
admin.site.register(models.EmailRecipient)
admin.site.register(models.CoreEmail)
