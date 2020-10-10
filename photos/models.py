from django.db import models

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
    photo = models.ImageField(upload_to = 'images/',null=True)
    image_name=models.CharField(max_length=30)
    image_description=models.TextField()
    image_location = models.ForeignKey(Location,on_delete=models.CASCADE, null=True)
    image_category = models.ForeignKey(Category,on_delete=models.CASCADE, null=True)
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image_name
    
    def save_image(self):
        self.save()

    @classmethod
    def save_image(cls):
        photos=cls.objects.filter()
        return photos

    @classmethod
    def location(cls,location): 
        images=Image.objects.filter(location=location)
        return images

    @classmethod
    def search_by_image_category(cls,search_term):
        photos = cls.objects.filter(image_category__icontains=search_term)
        return photos


