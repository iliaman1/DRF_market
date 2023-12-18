from rest_framework.generics import CreateAPIView

from .serializers import UserSerializer
from .tasks import confirmation_email


class UserCreateView(CreateAPIView):
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = serializer.save()

        confirmation_email.send(user.pk)
