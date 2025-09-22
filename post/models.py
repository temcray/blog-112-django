from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reversed("post_detail", args=[self.id])