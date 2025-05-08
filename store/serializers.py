from rest_framework import serializers
from .models import Category, SubCategory, Product, ProductImage


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'image', ]


class SubCategorySerializer(serializers.ModelSerializer):
    parent_category = CategorySerializer()

    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'slug', 'image', 'parent_category', ]


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'size', ]


class ProductSerializer(serializers.ModelSerializer):
    subcategory = SubCategorySerializer()
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'slug', 'subcategory', 'price', 'images', ]
