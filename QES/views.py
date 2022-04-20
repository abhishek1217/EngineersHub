from django.shortcuts import render, HttpResponse
from . models import Questions


def home(request):
    context = {
        "questions" : Questions.objects.all()
    }
    return render(request,'home.html',context)