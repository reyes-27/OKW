from rest_framework import serializers
from .models import Membership, CustomerMembership

class MembershipSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
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

class CustomerMembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerMembership
        fields = "__all__"
        read_only_fields = [
            "end_date",
        ]