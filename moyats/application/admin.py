from django.contrib import admin
from .models import ApplicationQuestion, Application, ScoreCard, ScoreCardItem, ReviewStep, ScoreCardReivewCategory, ReviewStepSet

admin.site.register(Application)
admin.site.register(ApplicationQuestion)
admin.site.register(ScoreCardReivewCategory)
admin.site.register(ScoreCard)
admin.site.register(ScoreCardItem)
admin.site.register(ReviewStep)
admin.site.register(ReviewStepSet)