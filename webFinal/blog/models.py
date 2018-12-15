from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse





class sketches(models.Model):
    title = models.CharField(max_length = 200)
    author = models.ForeignKey(User,on_delete = models.CASCADE, related_name = 'author')
    images = models.ImageField()