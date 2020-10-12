from django.test import TestCase
from .models import Location, Category, Image

# Create your tests here.
class LocationTestClass(TestCase):

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_location=Location(location='Nairobi')

    def test_instance(self):
        '''
        Test case to test if the object is initialized properly
        '''
        self.assertTrue(isinstance(self.new_location,Location))

    def test_save_method(self):
        '''
        Test case to test the save functionality
        '''
        self.new_location.save_location()
        location=Location.objects.all()
        self.assertTrue(len(location)>0)
    
    def test_delete_location(self):
        before = Location.objects.count()
        self.new_location.delete_category()
        after = Location.objects.count()
        self.assertTrue(before > after)
    
    def tearDown(self):
        Location.objects.all().delete()

class CategoryTestClass(TestCase):

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_category=Category(category='Travel')

    def test_instance(self):
        '''
        Test case to test if the object is initialized properly
        '''
        self.assertTrue(isinstance(self.new_category,Category))

    def test_save_method(self):
        '''
        Test case to test the save functionality
        '''
        self.new_category.save_category()
        category=Category.objects.all()
        self.assertTrue(len(category)>0)
    
    def test_delete_category(self):
        before = Category.objects.count()
        self.new_category.delete_category()
        after = Category.objects.count()
        self.assertTrue(before > after)
    
    def tearDown(self):
        Category.objects.all().delete()

class ImageTestClass(TestCase):

    def setUp(self):
        '''
        Set up method to run before each test cases and save.
        '''
        self.new_location=Location(location='Nairobi')
        self.new_location.save_location()

        self.new_category=Category(category='Travel')
        self.new_category.save_category()

        self.new_image=Image(image_name='Lake',image_description='A beautiful lake',image_location=self.new_location,image_category=self.new_category)
        self.new_image.save()

    def test_instance(self):
        '''
        Test case to test if the object is initialized properly
        '''
        self.assertTrue(isinstance(self.new_image,Image))

    def test_save_method(self):
        '''
        Test case to test the save functionality
        '''
        self.new_image.save()
        image=Image.objects.all()
        self.assertTrue(len(image)>0)

    def test_image_instance(self):
        self.assertTrue(isinstance(self.new_image, Image))

    def test_image_update(self):
        pass

    def test_image_delete(self):
        pass

    def test_search_image_category(self):
        pass


    def test_get_image_by_id(self):
        pass

    def tearDown(self):
        '''
        Cleaning up stuff from the setUp method
        '''
        Location.objects.all().delete()
        Category.objects.all().delete()
        Image.objects.all().delete()

    
