from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=20)
    categories = models.CharField(max_length=50)
    age = models.IntegerField()
    reputation = models.IntegerField(default=None)
    phone = models.CharField(max_length=10)
    profile_pic = models.ImageField(default='default.jpg',upload_to='profile_pics')