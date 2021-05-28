from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from cloudinary.models import CloudinaryField

class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = CloudinaryField('image')
    link = models.CharField(max_length=100)
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project_details', args=[str(self.id)])