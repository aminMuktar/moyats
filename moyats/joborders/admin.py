from . import models
from django.contrib import admin

admin.site.register(models.JobOrderType)
admin.site.register(models.JobOrderCategory)
admin.site.register(models.JobDetail)
admin.site.register(models.JobOrder)
