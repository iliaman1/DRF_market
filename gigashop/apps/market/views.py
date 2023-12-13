from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Product, Category, Review
from .serializers import ProductSerializer, ReviewSerializer
from .permissions import IsAdminOrReadOnly
from .paginators import ProductPaginator


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = ProductPaginator

    def get_queryset(self):
        if pk := self.kwargs.get('product_pk'):
            return Product.objects.filter(pk=pk)

        return Product.objects.all()

    @action(methods=['get'], detail=False)
    def category(self, request):
        return Response({'categoryes': list(Category.objects.values('title'))})


class ReviewListCreate(ListCreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return Review.objects.select_related('product').filter(product=self.kwargs.get('product_pk'))

    def get_serializer_context(self):
        context = super().get_serializer_context()

        context['author_id'] = self.request.user.pk
        context['product_id'] = self.kwargs['product_pk']

        return context
