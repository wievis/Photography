from django.db import models

class Photo(models.Model):
    image = models.ImageField(upload_to='photography_portfolio_page')
    order = models.IntegerField(default=0)
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