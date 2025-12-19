from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArtistViewSet, ArtistAvailabilityViewSet, ArtistCategoryViewSet

router = DefaultRouter()
router.register(r'categories', ArtistCategoryViewSet, basename='artist-category')
router.register(r'availability', ArtistAvailabilityViewSet, basename='artist-availability')
router.register(r'', ArtistViewSet, basename='artist')

urlpatterns = [
    path('', include(router.urls)),
]
