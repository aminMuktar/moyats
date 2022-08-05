from .models import Activity
from .types import ActivityType
from django.contrib.contenttypes.models import ContentType
from core.models import Notification

# create activity for candidate type


def create_candidate_activity(candidiate, activity_type, annotation, user):
    activity = Activity.objects.create(
        user=user,
        organization=candidiate.organization,
        cand_activity_type=activity_type,
        activity_type="ca",
        annotation=annotation,
        content_type=ContentType.objects.get_for_model(candidiate),
        object_id=candidiate.id
    )
    Notification.objects.create(a_from=user, action="Candidate created")
    
    return activity
