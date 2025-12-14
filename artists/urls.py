from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArtistViewSet, ArtistAvailabilityViewSet

router = DefaultRouter()
router.register(r'', ArtistViewSet, basename='artist')
router.register(r'availability', ArtistAvailabilityViewSet, basename='artist-availability')

urlpatterns = [
    path('', include(router.urls)),
]
