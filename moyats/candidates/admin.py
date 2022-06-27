from . import models
from django.contrib import admin
from core.models import Attachment

admin.site.register(Attachment)
admin.site.register(models.CandidateSource)
admin.site.register(models.SocialMedia)
admin.site.register(models.CandidateProfile)
admin.site.register(models.WorkHistory)
admin.site.register(models.QualificationChecklist)
admin.site.register(models.CandidateQualification)
admin.site.register(models.Candidate)
