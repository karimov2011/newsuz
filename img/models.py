from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField()
    image = models.ImageField(upload_to="img/", blank=True)
    create_date = models.DateTimeField(auto_now=True) 
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return(self.title)
    