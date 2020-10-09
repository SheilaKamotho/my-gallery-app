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

class ImageTestClass(TestCase):

    def setUp(self):
        '''
        Set up method to run before each test cases.
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
        self.assertTrue(isinstance(self.new_category,Category))

    def test_save_method(self):
        '''
        Test case to test the save functionality
        '''
        self.new_category.save_category()
        category=Category.objects.all()
        self.assertTrue(len(category)>0)

