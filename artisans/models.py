from django.db import models

class Artisan(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)  # e.g., plumber, electrician, etc.
    location = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    description = models.TextField()
    profile_picture = models.ImageField(upload_to='artisan_pics/', blank=True, null=True)

    def __str__(self):
        return self.name