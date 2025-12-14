from django.db import models
from django.conf import settings

class Artist(models.Model):
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=50)
    description = models.TextField()
    specialization = models.CharField(max_length=100, blank=True, null=True)
    experience_level = models.CharField(max_length=50, blank=True, null=True)
    
    phone = models.CharField(max_length=20, blank=True, null=True)
    location = models.CharField(max_length=25)
    offers_home_service = models.BooleanField(default=False)
    
    instagram = models.URLField(blank=True, null=True)
    tiktok = models.URLField(blank=True, null=True)
    portfolio_images = models.JSONField(default=list, blank=True)
    
    # Ownership
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='artist_profiles')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ArtistAvailability(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='availabilities')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        unique_together = ('artist', 'date', 'start_time')

    def __str__(self):
        return f"{self.artist.name} - {self.date} ({self.start_time} - {self.end_time})"
