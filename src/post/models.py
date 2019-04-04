from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 200)
    body = models.TextField()
    image = models.ImageField(default = 'noimage.jpg', upload_to='post_pics')
    author = models.ForeignKey(User, on_delete = models.CASCADE)


    def __str__(self):
        return f'{self.title} by {self.author.first_name} {self.author.last_name}'