from django.db import models
import datetime as dt

# Create your models here.
class Location(models.Model):
    """
    Class that generates new instances of location
    """
    location=models.CharField(max_length=30)

    def __str__(self):
        return self.location

    def save_location(self):
        self.save()

class Category(models.Model):
    """
    Class that generates new instances of location
    """
    category=models.CharField(max_length=30)
    
    def __str__(self):
        return self.category

    def save_category(self):
        self.save()


class Image(models.Model):
    """
    Class that generates new instance of images
    """
    image_name=models.CharField(max_length=30)
    image_description=models.CharField(max_length=1000)
    image_location = models.ForeignKey(Location,on_delete=models.CASCADE, null=True)
    image_category = models.ForeignKey(Category,on_delete=models.CASCADE, null=True)
    post_date = models.DateTimeField(auto_now_add=True)
    