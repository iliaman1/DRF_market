from rest_framework import serializers
from .models import Product, Review


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'picture', 'category', 'price', 'stock')


class ReviewSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Review
        fields = ('author_name', 'author', 'text', 'update_at')
        read_only_fields = ('author',)

    def create(self, validated_data):
        validated_data['author_id'] = self.context['author_id']
        validated_data['product_id'] = self.context['product_id']

        return super().create(validated_data)
