from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=20)
    age = models.IntegerField(null=True)
    reputation = models.IntegerField(blank=True,null=True)
    phone = models.CharField(max_length=10)
    profile_pic = models.ImageField(default='default.png',upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'