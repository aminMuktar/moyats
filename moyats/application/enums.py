from django.db import models
from django.utils.translation import gettext_lazy as _

class SaveApplicationDetailTypes(models.TextChoices):
    APPLICATION_ONLY = 'ao', _('Application Only')
    RESUME = 'rs', _('Resume')
    FIRST_NAME = 'fn', _('First Name')
    MIDDLE_NAME = 'mn', _('Middle Name')
    LAST_NAME = 'ln', _('Last Name')
    PHONE_HOME = 'ph', _('Home Phone')
    PHONE_MOBILE = 'pm', _('Mobile Phone')
    PHONE_WORK = 'pw', _('Work Phone')
    ADDRESS = 'ad', _('Address')
    CITY = 'ct', _('City')
    STATE = 'st', _('State')
    ZIP_CODE = 'zc', _('Zip Code')
    SOURCE = 'sr', _('Source')
    KEY_SKILLS = 'ks', _('Key Skills')
    CURRENT_EMPLOYEER = 'ce', _('Current Employeer')
    EMAIL = 'em', _('Email')
    DESIRED_PAY = 'dp', _('Desired Pay')
    CURRENT_PAY = 'cp', _('Current Pay')
    COUNTRY = 'cn', _('Country')
    WORK_HISTORY = 'wh', _('Work History')
    SOCIAL_MEDIA = 'sm', _('Social Media')
