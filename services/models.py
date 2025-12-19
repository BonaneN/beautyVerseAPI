from django.db import models
from artists.models import Artist, ArtistCategory

class Service(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='services')
    category = models.ForeignKey(ArtistCategory, on_delete=models.CASCADE, related_name='services')
    is_home_service = models.BooleanField(default=False)
    portfolio_images = models.JSONField(default=list, blank=True) # Max 3 images validation in Serializer
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('artist', 'category')

    def __str__(self):
        return f"{self.artist} - {self.category.name}"
