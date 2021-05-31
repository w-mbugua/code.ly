from django.test import TestCase
from .models import Project
from django.contrib.auth import get_user_model


class ProjectModelTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='Joe', email='jdoe@anon.com', password='bananas')
        self.project = Project.objects.create(title='project noir', description='testing project', link='noir.com', creator=self.user)
    
    def test_toString(self):
        self.assertEqual(str(self.project), self.project.title)
    
    def test_project_details(self):
        self.assertEqual(self.project.title, 'project noir')
        self.assertEqual(self.project.description, 'testing project')
        self.assertEqual(self.project.link, 'noir.com')
        self.assertEqual(self.project.creator.username, 'Joe')


