from rest_framework import serializers
from .models import Cart, CartProduct, Category, Subcategory, Product


class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartProduct
        fields = ['product', 'quantity']


class CartSerializer(serializers.ModelSerializer):
    products = CartProductSerializer(many=True, source='cartproduct_set')

    class Meta:
        model = Cart
        fields = ['id', 'user', 'products', 'created_at', 'updated_at']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'image']


class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ['id', 'name', 'slug', 'image', 'category']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'slug', 'price', 'image_small', 'image_medium', 'image_large', 'subcategory']
