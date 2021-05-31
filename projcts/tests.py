from django.test import TestCase
from .models import Project, Review
from django.contrib.auth import get_user_model


class ProjectModelTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='Joe', email='jdoe@anon.com', password='bananas')
        self.project = Project.objects.create(title='project noir', description='testing project', link='noir.com', creator=self.user)
        self.review1 = Review.objects.create(project = self.project, reviewer = self.user, design=10, usability=9, content=10)
    
    def test_instanciation(self):
        self.assertTrue(isinstance(self.project, Project))

    def test_toString(self):
        self.assertEqual(str(self.project), self.project.title)
    
    def test_project_details(self):
        self.assertEqual(self.project.title, 'project noir')
        self.assertEqual(self.project.description, 'testing project')
        self.assertEqual(self.project.link, 'noir.com')
        self.assertEqual(self.project.creator.username, 'Joe')
    
    def test_get_reviews(self):
        self.assertEqual(self.project.get_reviews()[0], self.review1)
    
    def test_get_design_rating(self):
        self.assertEqual(self.project.get_design_rating(), self.review1.design)
    
    def test_get_usability_rating(self):
        self.assertEqual(self.project.get_usability_rating(), self.review1.usability)
    
    def test_get_content_rating(self):
        self.assertEqual(self.project.get_content_rating(), self.review1.content)

class ReviewModelTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='newuser', email='user@testing.com', password='testing')
        self.project = Project.objects.create(title='test project', description="new project alert", link='project.com', creator=self.user)
        
        self.review = Review.objects.create(project = self.project, reviewer=self.user, design=10, usability=9, content=10)

    def test_instanciation(self):
        self.assertTrue(isinstance(self.review, Review))
    
    def test_toString(self):
        self.assertEqual(str(self.review), f"{self.review.project} - {self.review.reviewer}")

