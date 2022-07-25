from .models import Activity
from .types import ActivityType
from django.contrib.contenttypes.models import ContentType

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
    return activity
