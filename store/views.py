from rest_framework import generics, viewsets

from store.models import Category, SubCategory, Product
from store.serializers import CategorySerializer, SubCategorySerializer, ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.select_related('parent_category').all()
    serializer_class = SubCategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.select_related('subcategory__parent_category').prefetch_related('images').all()
    serializer_class = ProductSerializer
