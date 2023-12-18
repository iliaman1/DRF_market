from django.urls import path

from apps.accounts.views import UserCreateView

urlpatterns = [
    path('create', UserCreateView.as_view(), name='accounts-create')
]
