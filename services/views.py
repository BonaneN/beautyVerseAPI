from rest_framework import viewsets, permissions, status, serializers
from rest_framework.response import Response
from .models import Service
from .serializers import ServiceSerializer

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.artist.created_by == request.user

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['category__name', 'artist__brand_name']

    def get_queryset(self):
        queryset = super().get_queryset()
        location = self.request.query_params.get('location')
        home_service = self.request.query_params.get('is_home_service')
        
        if location:
            queryset = queryset.filter(artist__location__icontains=location)
        if home_service:
            is_home = home_service.lower() == 'true'
            queryset = queryset.filter(is_home_service=is_home)
            
        return queryset

    def perform_create(self, serializer):
        user = self.request.user
        artist = user.artist_profiles.first()
        
        if not artist:
            raise serializers.ValidationError({"detail": "You must create an Artist profile first."})
            
        serializer.save(artist=artist)
