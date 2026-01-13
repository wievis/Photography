from django.db import models
from cloudinary.models import CloudinaryField

class Photo(models.Model):
    image = CloudinaryField('image', folder='photography_portfolio_page')
    order = models.IntegerField(default=0)
    aparat = models.CharField(max_length=80, blank=True)
    ogniskowa = models.CharField(max_length=20, blank=True)
    naswietlanie = models.CharField(max_length=20, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['order', '-created']
    
    def __str__(self):
        return f"Photo {self.id}"
    
class Visitor(models.Model):
    ip = models.GenericIPAddressField()
    ua = models.TextField()
    ref = models.TextField(null=True)
    country = models.CharField(max_length=100, null=True)
    at = models.DateTimeField(auto_now_add=True)