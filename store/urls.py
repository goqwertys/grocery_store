from rest_framework.routers import DefaultRouter

from store.views import CategoryViewSet, SubCategoryViewSet, ProductViewSet

router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('subcategories', SubCategoryViewSet)
router.register('products', ProductViewSet)

urlpatterns = router.urls
