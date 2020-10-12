from django.db import models

# Create your models here.
class Location(models.Model):
    """
    Class that generates new instances of location
    """
    location=models.CharField(max_length=30)

    
    @classmethod
    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def update_location(self):
        self.update()

    def __str__(self):
        return self.location

    class Meta:
        db_table = 'location'

class Category(models.Model):
    """
    Class that generates new instances of location
    """
    category=models.CharField(max_length=30)

    @classmethod
    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def update_category(self):
        self.update()


    def __str__(self):
        return self.category

    class Meta:
        db_table = 'category'

    
class Image(models.Model):
    """
    Class that generates new instance of images
    """
    photo = models.ImageField(upload_to = 'images/',null=True)
    image_name=models.CharField(max_length=30)
    image_description=models.TextField()
    image_location = models.ForeignKey(Location,on_delete=models.CASCADE)
    image_category = models.ForeignKey(Category,on_delete=models.CASCADE)
    category1 = models.CharField(max_length=30)
    post_date = models.DateTimeField(auto_now_add=True)
    
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
        photos = cls.objects.filter(category1__icontains=search_term)
        return photos

    @classmethod
    def update_image(self, image_name=image_name, imae_category=None):
        self.image_name = image_name if image_name else self.image_name
        self.category1 = category1 if category1 else self.category1
        self.save()
    
    @classmethod
    def get_image_by_id(cls, id):
        return cls.objects.get(pk=id)

    def delete_image(self):
        self.delete()

    def __str__(self):
        return self.image_name

