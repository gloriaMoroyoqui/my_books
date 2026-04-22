from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255)

    

    def __str__(self):
        return self.title
    
class Post(models.Model):

    ACTIVATE = 'activate'
    DRAFT = 'draft'

    CHOICES_STATUS = [
        (ACTIVATE, 'activate'),
        (DRAFT, 'draft')
    ]

    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    intro = models.TextField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=ACTIVATE)
    image = models.ImageField(upload_to='upload/', blank=True, null=True)

    def __str__(self):
        return self.title