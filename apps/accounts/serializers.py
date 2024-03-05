from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import Customer
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    # AuthUser = TypeVar('AuthUser', get_user_model(), TokenUser)
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["username"] = user.username
        # token["user_membership"] = user.customer.membership.model.level
        return token

class ShortCustomerSerializer(serializers.ModelSerializer):
    def get_full_name(self, obj):
        return obj.full_name
    full_name = serializers.SerializerMethodField()
    class Meta:
        model = Customer
        fields = [
            "id",
            "profile_pic",
            "full_name",
            "reputation",
            "is_seller",
        ]

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"