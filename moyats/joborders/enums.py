from django.db import models
from django.utils.translation import gettext_lazy as _


class PositionTypes(models.TextChoices):
    REMOTE = 'rm', _('Remote')
    FULL_TIME = 'fl', _('Full Time')
    PART_TIME = 'pt', _('Part Time')
    FREELANCE = 'fr', _('Freelance')
    WITH_RELOCATION = 'rl', _('With Relocation')
