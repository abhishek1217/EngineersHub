from django.shortcuts import render, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from . models import Questions


# def home(request):
#     context = {
#         "questions" : Questions.objects.all()
#     }
#     return render(request,'home.html',context)

class QuestionsListView(ListView):
    model = Questions
    template_name = 'home.html' # <app>/<model>_<viewtype>.html
    context_object_name = "questions"
    ordering = ['-date_posted']

class QuestionsDetailView(DetailView):
    model = Questions
    template_name = 'qna.html'

class QuestionsCreateView(LoginRequiredMixin, CreateView):
    model = Questions
    fields = ['title','content','category']
    template_name = 'add_question.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class QuestionsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Questions
    fields = ['title','content','category']
    template_name = 'add_question.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        question = self.get_object()
        if self.request.user == question.author:
            return True
        return False
# def qna(request):
#     return render(request,'qna.html')