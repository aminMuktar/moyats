from django.db import models
from django.core.validators import RegexValidator

class BaseContact(models.Model):
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    cell_number = models.CharField(validators=[phone_regex], max_length=17)
    work_number = models.CharField(
        validators=[phone_regex], max_length=17, blank=True, null=True)
    home_number = models.CharField(
        validators=[phone_regex], max_length=17, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.cell_number)

class Color(models.Model):
    hex = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.hex