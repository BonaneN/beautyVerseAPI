from rest_framework import serializers
from .models import Artist, ArtistAvailability, ArtistCategory
from services.serializers import ServiceSerializer

class ArtistCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtistCategory
        fields = ['id', 'name', 'slug']

class ArtistAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtistAvailability
        fields = ['id', 'date', 'time', 'is_booked']
        read_only_fields = ['is_booked']

class ArtistSerializer(serializers.ModelSerializer):
    availabilities = ArtistAvailabilitySerializer(many=True, read_only=True)
    services = ServiceSerializer(many=True, read_only=True)
    
    class Meta:
        model = Artist
        fields = [
            'id', 'name', 'brand_name', 'phone', 'whatsapp_contact', 
            'location', 'instagram', 'tiktok', 'created_by',
            'availabilities', 'services', 'created_at'
        ]
        read_only_fields = ['created_by', 'created_at']

    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)
