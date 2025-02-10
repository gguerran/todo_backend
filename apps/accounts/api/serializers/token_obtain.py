from rest_framework_simplejwt.serializers import TokenObtainPairSerializer as JWTTokenObtainPairSerializer
from apps.accounts.models import Student


class TokenObtainPairSerializer(JWTTokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        serializer = self.user.serializer_class
        user = self.user
        user_data = serializer(user, context=self.context).data
        request = self.context.get("request")
        user_data.update(
            {"profile_image": f"{request.scheme}://{request.META['HTTP_HOST']}{user_data['profile_image']}"}
        )
        data.update({"user": user_data})
        return data
