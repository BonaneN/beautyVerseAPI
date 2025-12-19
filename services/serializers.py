from rest_framework import serializers
from .models import Service
from artists.models import ArtistCategory

class ServiceSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=ArtistCategory.objects.all(), source='category', write_only=True
    )
    
    class Meta:
        model = Service
        fields = ['id', 'category_name', 'category_id', 'is_home_service', 'portfolio_images']

    def validate_portfolio_images(self, value):
        if len(value) > 3:
            raise serializers.ValidationError("Maximum 3 portfolio images allowed for this service.")
        return value
