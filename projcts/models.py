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
    pub_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project_details', args=[str(self.id)])
    
    def get_design_rating(self):
        reviews = self.reviews.all()
        total_design = 0
        avg = 0
        for review in reviews:
            total_design += review.design
            avg = total_design / reviews.count()
        return avg

    def get_usability_rating(self):
        reviews = self.reviews.all()
        total_usability = 0
        for review in reviews:
            total_usability += review.usability
        return total_usability
    
    def get_content_rating(self):
        reviews = self.reviews.all()
        total_content = 0
        for review in reviews:
            total_content += review.content
        return total_content



RATING_CHOICES = ((1, '1'),(2, '2'),(3, '3'),(4, '4'),(5, '5'),(6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'))

class Review(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='reviews')
    pub_date = models.DateTimeField(auto_now_add=True)
    reviewer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    design = models.IntegerField(choices=RATING_CHOICES)
    usability = models.IntegerField(choices=RATING_CHOICES)
    content = models.IntegerField(choices=RATING_CHOICES)

    def __str__(self):
        return f"{self.project} - {self.reviewer}"
    
    def get_absolute_url(self):
        return reverse('project_list')
    
    def total_rating(self):
        return self.design + self.usability + self.content