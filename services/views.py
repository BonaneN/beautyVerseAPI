from rest_framework import viewsets, permissions
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

    def perform_create(self, serializer):
        artist = serializer.validated_data['artist']
        if artist.created_by != self.request.user:
            raise permissions.PermissionDenied("You do not own this artist profile.")
        serializer.save()
