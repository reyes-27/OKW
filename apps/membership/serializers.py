from rest_framework.serializers import (
    HyperlinkedModelSerializer,
    HyperlinkedIdentityField,)
from .models import Membership

class MembershipSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='membership-detail',
        lookup_field='slug',
        lookup_url_kwarg='slug',
        )
    class Meta:
        model = Membership
        fields = [
            'url',
            'slug',
            'name',
            'level',
            'desc',
            'duration',
        ]