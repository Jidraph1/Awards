from django.test import TestCase
from django.contrib.auth.models import User
from .models import Project,Profile, Review

# Create your tests here.
class ProfielTestCase(TestCase):
    def setUp(self):

        self.new_profile = Profile(id=1, user='Jid', profile_picture='example.jpg', bio='Dare to live',
        email='email@gmail.com', phone_number='072833375', username='jidraph')

    def tearDown(self):
        Profile.objects.all().delete()

    def test_is_instance(self):
        self.assertTrue(isinstance(self.new_profile, Profile))

    def test_save_method(self):
        self.new_profile.save_profile()
        all_obj = Profile.objects.all()
        self.assertTrue(len(all_obj) > 0)
        


class ProfileTestCase(TestCase):
    def setUp(self):
        self.new_project = Project(id=1, user='Jid', title ='To live to love', 
        image = 'image.jpg', description= 'new projects loading',link = 'ww.insta.com', county='Kenya')

    def tearDown(self):
        Project.objects.all().delete()

    def test_is_instance(self):
        self.assertTrue(isinstance(self.new_project,Project))

    def test_save_method(self):
        self.new_project.save_project()
        all_obj = Project.objects.all()
        self.assertTrue(len(all_obj)>0)  

class ReviewTestCases(TestCase):
    def setUp(self):      
        self.new_review = Review(id=1,user='Jid',project='Instagram',design='1',usability='1',content='1',overall='1',comment='comment')
        self.new_review.save_review()
        
    def test_is_instance(self):
        self.assertTrue(isinstance(self.new_review,Review))
                
        