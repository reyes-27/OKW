from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.serializers import HyperlinkedModelSerializer, HyperlinkedIdentityField
from .models import Customer
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    # AuthUser = TypeVar('AuthUser', get_user_model(), TokenUser)
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["username"] = user.username
        # token["user_membership"] = user.customer.membership.model.level
        return token

class CustomerSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(view_name="customer-detail")
    class Meta:
        model = Customer
        fields = "__all__"