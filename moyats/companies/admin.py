from django.contrib import admin
from .models import CompanyStatus, Company, CompanyContact

admin.site.register(Company)
admin.site.register(CompanyStatus)
admin.site.register(CompanyContact)