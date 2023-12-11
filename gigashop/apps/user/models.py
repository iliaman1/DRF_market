from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext as _

from core.models import BaseModel


class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, verbose_name=_('Никнэйм'))
    avatar = models.ImageField(
        null=True,
        blank=True,
        upload_to='images/profile/%Y/%m/%d/',
        default='images/product/default_avatar.png',
        verbose_name=_('Аватар')
    )
    email = models.EmailField(max_length=64, verbose_name=_('Почта'))

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created_at']
        verbose_name = _('Профиль')
        verbose_name_plural = _('Профили')
