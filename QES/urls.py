from django.contrib import admin
from django.urls import path
from .views import QuestionsListView,QuestionsDetailView,QuestionsCreateView,QuestionsUpdateView,UpvoteQuest,UpvoteQuest2
from QES import views

urlpatterns = [
    path('',QuestionsListView.as_view(),name="home"),
    path('qna/<int:pk>/',QuestionsDetailView.as_view(),name="qna"),
    path('qna/<int:pk>/update',QuestionsUpdateView.as_view(),name="question-update"),
    path('qna/add/',QuestionsCreateView.as_view(),name="add-question"),
    path('upvote/<int:pk>/',UpvoteQuest,name="upvote_quest"),
    path('upvote2/<int:pk>/',UpvoteQuest2,name="upvote_quest2")
    # path('qna/',views.qna,name="qna"),
]

