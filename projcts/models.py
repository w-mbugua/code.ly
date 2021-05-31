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
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project_details', args=[str(self.id)])
    
    def get_reviews(self):
        reviews = self.reviews.all()
        reviewers = []
        for review in reviews:
            if review.reviewer in reviewers:
                review.delete()
            else:
                reviewers.append(review.reviewer)
        return reviews
    
    def get_design_rating(self):
        reviews = self.get_reviews()
        total_design = 0
        avg = 0
        r = []
        for review in reviews:
            total_design += review.design
            avg = total_design / reviews.count()
            r.append(review.reviewer)
        return avg

    def get_usability_rating(self):
        reviews = self.get_reviews()
        total_usability = 0
        avg = 0
        for review in reviews:
            total_usability += review.usability
            avg = total_usability / reviews.count()
        return avg
    
    def get_content_rating(self):
        reviews = self.get_reviews()
        total_content = 0
        avg = 0
        for review in reviews:
            total_content += review.content
            avg = total_content / reviews.count()
        return avg
    
    @classmethod
    def search_project(cls, word):
        obj = cls.objects.filter(title__icontains=word)
        return obj
    
        

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
    

