from django.db import models
from cloudinary.models import CloudinaryField
from projcts.models import Project
from users.models import CustomUser
from django.contrib.auth import get_user_model
from django.urls import reverse

class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='profile')
    photo = CloudinaryField('image')
    bio = models.TextField()

    def __str__(self):
        return f"{self.user} profile"
    
    def get_absolute_url(self):
        return reverse('profile', args=[str(self.pk)])

    
