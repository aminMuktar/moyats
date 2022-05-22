from . import models
from django.contrib import admin

admin.site.register(models.Trigger)
admin.site.register(models.PipelineStatus)
admin.site.register(models.PipelineSetup)
admin.site.register(models.PipelineWorkflow)
