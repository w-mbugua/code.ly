from django.db import models
from cloudinary.models import CloudinaryField
from projcts.models import Project
from users.models import CustomUser
from django.urls import reverse

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    photo = CloudinaryField('image')
    bio = models.TextField()

    def __str__(self):
        return f"{self.user} profile"
    
    def get_absolute_url(self):
        return reverse('profile', args=[str(self.pk)])

    
