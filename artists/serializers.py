from rest_framework import serializers
from .models import Artist, ArtistAvailability
from services.serializers import ServiceSerializer

class ArtistAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtistAvailability
        fields = ['id', 'date', 'start_time', 'end_time']

class ArtistSerializer(serializers.ModelSerializer):
    availabilities = ArtistAvailabilitySerializer(many=True, read_only=True)
    services = ServiceSerializer(many=True, read_only=True)
    
    class Meta:
        model = Artist
        fields = [
            'id', 'name', 'category', 'description', 'specialization', 
            'experience_level', 'phone', 'location', 'offers_home_service',
            'instagram', 'tiktok', 'portfolio_images', 'created_by',
            'availabilities', 'services', 'created_at'
        ]
        read_only_fields = ['created_by', 'created_at']

    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)
