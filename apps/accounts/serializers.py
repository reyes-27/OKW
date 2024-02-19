from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    # AuthUser = TypeVar('AuthUser', get_user_model(), TokenUser)
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["username"] = user.username
        # token["user_membership"] = user.customer.membership.model.level
        return token
