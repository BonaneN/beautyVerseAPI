from rest_framework import serializers
from .models import Product, ProductCategory

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['id', 'name', 'slug', 'created_at']
        read_only_fields = ['slug', 'created_at']

class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    created_by_username = serializers.CharField(source='created_by.username', read_only=True)

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'description', 'price', 'discount_percentage',
            'final_price', 'shop_location', 'delivery_available',
            'category', 'category_name', 'created_by', 'created_by_username',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['final_price', 'created_by', 'created_at', 'updated_at']
