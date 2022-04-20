from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Questions(models.Model):
    title = models.TextField()
    content = models.TextField()
    category = models.CharField(max_length=255)
    upvotes = models.IntegerField(null=True)
    downvotes = models.IntegerField(null=True)
    # date_posted = models.models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Answers(models.Model):
    answer = models.TextField()
    upvotes = models.IntegerField(null=True)
    downvotes = models.IntegerField(null=True)
    # date_posted = models.models.DateTimeField(default=timezone.now)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer
    
    


