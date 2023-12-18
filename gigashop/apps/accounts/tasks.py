import dramatiq
from django.contrib.auth.models import User


@dramatiq.actor
def confirmation_email(user_id: int):
    user = User.objects.get(pk=user_id)
    print(f'Привет из асинхронной хадачи, {user}')
