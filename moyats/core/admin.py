from . import models
from django.contrib import admin


class ActivityAdmin(admin.ModelAdmin):
    fields = ['organization', 'user', 'activity_type', 'annotation',
              'content_type', 'object_id', 'content_object', 'created_at', ]
    readonly_fields = ['created_at', 'content_object', ]

    class Meta:
        model = models.Activity


admin.site.register(models.Activity, ActivityAdmin)
admin.site.register(models.Notification)
