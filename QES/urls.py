from django.contrib import admin
from django.urls import path
from .views import QuestionsListView,QuestionsDetailView,QuestionsCreateView,QuestionsUpdateView
from QES import views

urlpatterns = [
    path('',QuestionsListView.as_view(),name="home"),
    path('qna/<int:pk>/',QuestionsDetailView.as_view(),name="qna"),
    path('postanswer/qna/<int:pk>/',QuestionsDetailView.as_view(),name="afterpost"),
    path('qna/<int:pk>/update',QuestionsUpdateView.as_view(),name="question-update"),
    path('qna/add/',QuestionsCreateView.as_view(),name="add-question"),
    path('upvoted/', views.upvoting, name='upvoted-question'),
    path('downvoted/', views.downvoting, name='downvoted-question'),
    path('postanswer/', views.PostAnswers, name='post-answer'),
    # path('qna/',views.qna,name="qna"),
]

