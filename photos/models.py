from django.db import models

# Create your models here.
class Location(models.Model):
    """
    Class that generates new instances of location
    """
    location=models.CharField(max_length=30)

class Category(models.Model):
    """
    Class that generates new instances of location
    """
    category=models.CharField(max_length=30)

class Image(models.Model):
    """
    Class that generates new instance of images
    """
    image_name=models.CharField(max_length=30)
    image_description=models.CharField(max_length=1000)
    image_location = models.ForeignKey(Location,on_delete=models.CASCADE)
    image_category = models.ForeignKey(Category,on_delete=models.CASCADE)
    