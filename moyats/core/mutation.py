from urllib import response
import graphene
from .models import Notification
from .types import NotificationType

class CreateNotification(graphene.Mutation):
    notification = graphene.Field(NotificationType)

    class Arguments:
        action = graphene.String()

    def mutate(self, info, action, **kwargs):
        notif = Notification.objects.create(a_from=info.context.user, action=action)

        return CreateNotification(notification=notif)

class UpdateNotification(graphene.Mutation):
    response = graphene.Boolean()

    class Arguments:
        notification_id = graphene.String()
        seen = graphene.Boolean()

    def mutate(self, info, notification_id, seen, **kwargs):
        notif = Notification.objects.filter(notification_id=notification_id)
        notif.update(seen=seen)

        return UpdateNotification(response=True)

class UpdateNotifications(graphene.Mutation):
    response = graphene.Boolean()

    class Arguments:
        cleared = graphene.Boolean()

    def mutate(self, info, cleared, **kwargs):
        Notification.objects.all().update(cleared=cleared)

        return UpdateNotifications(response=True)