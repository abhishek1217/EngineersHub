from django.contrib import admin
from django.urls import path
from .views import QuestionsListView,QuestionsDetailView,QuestionsCreateView,QuestionsUpdateView
from QES import views

urlpatterns = [
    path('',QuestionsListView.as_view(),name="home"),
    path('qna/<int:pk>/',QuestionsDetailView.as_view(),name="qna"),
    path('qna/<int:pk>/update',QuestionsUpdateView.as_view(),name="question-update"),
    path('qna/add/',QuestionsCreateView.as_view(),name="add-question"),
    path('upvoted/', views.upvoting, name='upvoted-question'),
    path('downvoted/', views.downvoting, name='downvoted-question'),
    # path('qna/',views.qna,name="qna"),
]

