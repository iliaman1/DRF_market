from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext as _

from core.models import BaseModel


class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(
        null=True,
        blank=True,
        upload_to='images/profile/%Y/%m/%d/',
        default='images/product/default_avatar.png',
        verbose_name=_('Аватар')
    )
    email_verified = models.BooleanField(
        default=False,
        verbose_name=_('Почта подтверждена')
    )

    class Meta:
        ordering = ['created_at']
        verbose_name = _('Профиль')
        verbose_name_plural = _('Профили')
