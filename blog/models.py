from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #when user is deleted, posts also get deleted thats why cascade is used 

    def __str__(self):
        return f"Post {self.author}:{self.title}"
    