from django.db import models

# Create your models here.

class CreateProperty(models.Model):
    title = models.CharField(max_length=255)
    discription = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bedroom = models.IntegerField()
    bathroom = models.IntegerField()
    status = models.CharField(max_length=50, choices=[('Sale','For sale'),('Rent', 'For rent')])
    locations = models.CharField(max_length=255)
    property_images = models.ImageField(upload_to='property_image')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    