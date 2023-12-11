from django.db import models
from django.contrib.auth.models import User
from core.models import BaseModel
from django.utils.translation import gettext_lazy as _


class Category(BaseModel):
    title = models.CharField(max_length=128, verbose_name=_('Категория'), unique=True)
    picture = models.ImageField(
        upload_to='images/category/%Y/%m/%d/',
        default='images/category/default_category.png',
        verbose_name=_('Изображение')
    )

    class Meta:
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')

    def __str__(self):
        return self.title

    def image(self):
        return {'src': self.picture.url, 'alt': self.title}


class Product(BaseModel):
    title = models.CharField(max_length=128, verbose_name=_('Название'), unique=True)
    picture = models.ImageField(
        upload_to='images/product/%Y/%m/%d/',
        default='images/product/default_product.png',
        verbose_name=_('Изображение')
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.PROTECT,
        verbose_name=_('Категория')
    )
    price = models.DecimalField(
        decimal_places=2,
        max_digits=100,
        default=0,
        verbose_name=_('Цена')
    )
    stock = models.PositiveIntegerField(
        default=0,
        verbose_name=_('На складе')
    )

    class Meta:
        verbose_name = _('Продукт')
        verbose_name_plural = _('Продукты')


class Review(BaseModel):
    product = models.ForeignKey('Product', on_delete=models.PROTECT, verbose_name=_('Продукт'))
    author = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name=_('Автор'))
    text = models.TextField(verbose_name=_('Текст'))

    class Meta:
        ordering = ['-created_at']
        verbose_name = _('Отзыв')
        verbose_name_plural = _('Отзывы')

    def __str__(self):
        return f'Комментарий от {self.author}'
