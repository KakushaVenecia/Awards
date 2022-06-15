from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, Category, Project, Rate 
# Create your tests here.

class ProjectTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='venecia',email="venee@gmail.com", bio="I am who I am ")
        self.post = Project.objects.create(name='Akan', photo='img.png', description='first project test',
                                        user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.post, Project))

    def test_save_profile(self):
        self.post.save_profile()
        post = Project.objects.all()
        self.assertTrue(len(post) > 0) 

    def test_search_by_category(self):
        self.post.save()
        post = Category.search_project('Akan')
        self.assertTrue(len(post) > 0)    

    def test_get_posts(self):
        self.post.save()
        posts = Project.all_posts()
        self.assertTrue(len(posts) > 0)

    def test_delete_profile(self):
        self.post.delete_profile()
        post = Project.search_project('Akan')
        self.assertTrue(len(post) < 1)


class RateTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='venee',email="ven@gmail.com")
        self.post = Project.objects.create(name='Django', photo='img.png', description='first project test',
                                        user=self.user)
        self.rating = Rate.objects.create(designrate=9, usabilityrate=10, contentrate=5, text=" This is great",user=self.user, post=self.post)

    def test_instance(self):
        self.assertTrue(isinstance(self.rating, Rate))

    def test_save_rating(self):
        self.rating.save_rating()
        rating = Rate.objects.all()
        self.assertTrue(len(rating) > 0)

    def test_get_post_rating(self, id):
        self.rating.save()
        rating = Rate.get_ratings(post_id=id)
        self.assertTrue(len(rating) == 1)
        

class ProfileTest(TestCase):
    def setUp(self):
        self.user = User(username='Ven',email="venee@gmail.com", password='password')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

    def test_save_user(self):
        self.user.save()

    def test_delete_user(self):
        self.user.delete()


     