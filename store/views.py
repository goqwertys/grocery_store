from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter

from store.models import Category, SubCategory, Product
from store.paginators import StandardResultsSetPagination
from store.permissions import IsAdminOrReadOnly
from store.serializers import CategorySerializer, SubCategoryReadSerializer, \
    SubCategoryWriteSerializer, ProductReadSerializer, ProductWriteSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().prefetch_related('subcategories')
    serializer_class = CategorySerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAdminOrReadOnly]
    lookup_field = 'slug'


class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.select_related('parent_category').all()
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAdminOrReadOnly]
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return SubCategoryReadSerializer
        return SubCategoryWriteSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.prefetch_related('images', 'subcategory__parent_category')
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAdminOrReadOnly]
    lookup_field = 'slug'

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['price', 'name', ]

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ProductReadSerializer
        return ProductWriteSerializer
