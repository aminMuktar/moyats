from urllib import response
import graphene
from core.helpers import org_exists
from accounts.models import BaseUser
from .models import Organization

from .inputs import OrgSetupInput
from .types import OrganizationType


class CreateOrganization(graphene.Mutation):
    class Arguments:
        input = OrgSetupInput(required=True)

    response = graphene.Field(OrganizationType)

    def mutate(root, info, input: OrgSetupInput):
        if org_exists(input.org_name):
            raise Exception("organization name is already taken")

        user = BaseUser.objects.filter(id=info.context.user.id)

        if user.first().setup_complete:
            raise Exception("Invalid request")

        user.update(first_name=input.first_name,
                    last_name=input.last_name,
                    )
        org = Organization(name=input.org_name,
                           verified=False,
                           org_type=input.org_type.lower(),
                           subdomain=input.subdomain
                           )
        org.save()
        user.first().organizations.add(org)
        user.update(setup_complete=True)
        return CreateOrganization(response=org)
