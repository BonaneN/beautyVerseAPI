from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Your app URLs
    path('beautyVerse/users/', include('users.urls')),
    path('beautyVerse/artists/', include('artists.urls')),
    path('beautyVerse/products/', include('products.urls')),
    path('beautyVerse/cart/', include('cart.urls')),
    path('beautyVerse/services/', include('services.urls')),
    path('beautyVerse/appointments/', include('appointments.urls')),

    # Swagger / API documentation
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc-ui'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
