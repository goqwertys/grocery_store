from rest_framework import serializers
from .models import Category, SubCategory, Product, ProductImage, CartItem, Cart


# --- ProductImage ---

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'size']


# --- SubCategory ---

class SubCategoryWriteSerializer(serializers.ModelSerializer):
    """Сериализатор для записи подкатегорий (принимает ID категории)"""
    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'slug', 'image', 'parent_category']


class CategoryShortSerializer(serializers.ModelSerializer):
    """Мини-сериализатор категории без вложенных подкатегорий"""
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']


class SubCategoryReadSerializer(serializers.ModelSerializer):
    """Сериализатор для чтения подкатегорий (вложенная категория)"""
    parent_category = CategoryShortSerializer(read_only=True)

    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'slug', 'image', 'parent_category']


# --- Category ---

class SubCategoryShortSerializer(serializers.ModelSerializer):
    """Мини-сериализатор подкатегорий (для отображения внутри категорий)"""
    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'slug']


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор категории с подкатегориями"""
    subcategories = SubCategoryShortSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'image', 'subcategories']


# --- Product ---

class SubCategoryShortSerializerForProduct(serializers.ModelSerializer):
    """ Мини-сериализатор подкатегории (для отображения в продукте) """
    parent_category = CategoryShortSerializer(read_only=True)

    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'slug', 'parent_category']


class ProductWriteSerializer(serializers.ModelSerializer):
    """ Сериализатор для создания/обновления продукта """
    class Meta:
        model = Product
        fields = ['id', 'name', 'slug', 'subcategory', 'price']


class ProductReadSerializer(serializers.ModelSerializer):
    """ Сериализатор для чтения продукта (вложенные данные)"""
    subcategory = SubCategoryShortSerializerForProduct(read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'slug', 'subcategory', 'price', 'images']


# --- CartItem ---

class CartItemReadSerializer(serializers.ModelSerializer):
    """ Сериализатор для чтения CartItem """
    product = ProductReadSerializer()

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', ]


class CartItemWriteSerializer(serializers.ModelSerializer):
    """ Сериализатор для записи CartItem """
    quantity = serializers.IntegerField(required=True)

    class Meta:
        model = CartItem
        fields = ['product', 'quantity', ]

    def validate_quantity(self, value):
        if value <= 0:
            raise serializers.ValidationError('Quantity must be grater than zero.')
        return value


class CartReadSerializer(serializers.ModelSerializer):
    """ Сериализатор для чтения Cart """
    items = CartItemReadSerializer(many=True, read_only=True)
    total_quantity = serializers.SerializerMethodField()
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items', 'total_quantity', 'total_price', ]

    def get_total_quantity(self, obj):
        return obj.total_items()

    def get_total_price(self, obj):
        return obj.total_price()
