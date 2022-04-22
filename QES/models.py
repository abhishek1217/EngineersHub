from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Questions(models.Model):
    title = models.TextField()
    content = models.TextField()
    category = models.CharField(max_length=255)
    upvotes = models.ManyToManyField(User,related_name="upvotes")
    # downvotes = models.IntegerField(null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "Question " + str(self.id)

    def get_absolute_url(self):
        return reverse("qna", kwargs={"pk": self.pk})
    
    def total_upvotes(self):
        return self.upvotes.count()
    


class Answers(models.Model):
    answer = models.TextField()
    ans_upvotes = models.ManyToManyField(User,related_name="ans_upvotes")
    # downvotes = models.IntegerField(null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "Answer " + str(self.id)

    
    


