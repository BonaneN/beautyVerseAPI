from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Artist, ArtistAvailability
from .serializers import ArtistSerializer, ArtistAvailabilitySerializer

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.created_by == request.user

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'location', 'category']

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    @action(detail=True, methods=['get'])
    def available_slots(self, request, pk=None):
        artist = self.get_object()
        date = request.query_params.get('date')
        if date:
            slots = artist.availabilities.filter(date=date, is_booked=False)
        else:
            slots = artist.availabilities.filter(is_booked=False)
        
        serializer = ArtistAvailabilitySerializer(slots, many=True)
        return Response(serializer.data)

class ArtistAvailabilityViewSet(viewsets.ModelViewSet):
    serializer_class = ArtistAvailabilitySerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        if self.action in ['list', 'retrieve']:
             return ArtistAvailability.objects.all()
        return ArtistAvailability.objects.filter(artist__created_by=self.request.user)

    def perform_create(self, serializer):
        artist = serializer.validated_data['artist']
        if artist.created_by != self.request.user:
            raise permissions.PermissionDenied("You do not own this artist profile.")
        serializer.save()
