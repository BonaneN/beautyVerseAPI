from rest_framework import viewsets, permissions, filters, serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Artist, ArtistAvailability, ArtistCategory
from .serializers import ArtistSerializer, ArtistAvailabilitySerializer, ArtistCategorySerializer

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.created_by == request.user

class ArtistCategoryViewSet(viewsets.ModelViewSet):
    queryset = ArtistCategory.objects.all()
    serializer_class = ArtistCategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'brand_name', 'location']

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
        user = self.request.user
        artist = user.artist_profiles.first()
        
        if not artist:
             raise serializers.ValidationError({"detail": "You must create an Artist profile first."})
             
        serializer.save(artist=artist)
