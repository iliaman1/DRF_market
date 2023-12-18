from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers

from apps.market.views import ProductViewSet, ReviewListCreate

router = routers.SimpleRouter()
router.register(r'product', ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
    path('product/<int:product_pk>/review', ReviewListCreate.as_view(), name='product-review')
]

urlpatterns = format_suffix_patterns(urlpatterns)