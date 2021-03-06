from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

categories = (
    ('CSE/ISE', 'CSE/ISE'),
    ('ECE', 'ECE'),
    ('MECH', 'MECH'),
    ('EEE','EEE'),
    ('CIVIL','CIVIL'),
    ('AI/ML','AI/ML'),
    ('AERO','AERO')
    )
class Questions(models.Model):
    title = models.TextField()
    content = models.TextField()
    category = models.CharField(max_length=255,choices=categories,default='CSE/ISE')
    upvotes = models.ManyToManyField(User,related_name="upvotes")
    downvoted = models.CharField(max_length=6,default='False')
    totalvotes = models.SmallIntegerField(default=0)
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return "Question " + str(self.id)

    def get_absolute_url(self):
        return reverse("qna", kwargs={"pk": self.pk})



class Answers(models.Model):
    answer = models.TextField()
    ans_upvotes = models.ManyToManyField(User,related_name="a_upvotes")
    downvoted = models.CharField(max_length=6,default='False')
    totalvotes = models.SmallIntegerField(default=0)
    date_posted = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "Answer " + str(self.id)

    
    


