from django.db import models

class Service(models.Model):
    artist = models.ForeignKey('artists.Artist', on_delete=models.CASCADE, related_name='services')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.DurationField(help_text="Duration of the service (e.g. 00:30:00)")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.artist.name}"
