from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Questions(models.Model):
    title = models.TextField()
    content = models.TextField()
    category = models.CharField(max_length=255)
    upvotes = models.ManyToManyField(User,related_name="qes_questions")
    downvotes = models.IntegerField(null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("qna", kwargs={"pk": self.pk})
    


class Answers(models.Model):
    answer = models.TextField()
    upvotes = models.IntegerField(null=True)
    downvotes = models.IntegerField(null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer
    
    


