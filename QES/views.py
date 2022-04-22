from django.shortcuts import render, HttpResponse, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from . models import Questions,Answers
from django.http import HttpResponseRedirect
from django.urls import reverse


# def home(request):
#     context = {
#         "questions" : Questions.objects.all()
#     }
#     return render(request,'home.html',context)

def UpvoteQuest(request,pk):
        quest = get_object_or_404(Questions, id=request.POST.get('question_id'))
        liked = False
        if quest.upvotes.filter(id=request.user.id).exists():
            quest.upvotes.remove(request.user)
            upvoted = False
        else:
            quest.upvotes.add(request.user)
            upvoted=True
        return HttpResponseRedirect(reverse('qna',args=[str(pk)]))

def UpvoteQuest2(request,pk):
        quest = get_object_or_404(Questions, id=request.POST.get('question_id'))
        liked = False
        if quest.upvotes.filter(id=request.user.id).exists():
            quest.upvotes.remove(request.user)
            upvoted = False
        else:
            quest.upvotes.add(request.user)
            upvoted=True
        return HttpResponseRedirect(reverse('home'))

class QuestionsListView(ListView):
    model = Questions
    template_name = 'home.html' # <app>/<model>_<viewtype>.html
    context_object_name = "questions"
    ordering = ['-date_posted']

    
    # Remember to give ordering based on the upvotes.

class QuestionsDetailView(DetailView):
    model = Questions
    template_name = 'qna.html'
    def get_context_data(self, **kwargs):
        context = super(QuestionsDetailView, self).get_context_data(**kwargs)
        grab = get_object_or_404(Questions, id=self.kwargs['pk'])
        upvoted = False

        if grab.upvotes.filter(id = self.request.user.id).exists():
            upvoted=True
        total_upvotes = grab.total_upvotes()
        context["total_upvotes"] =  total_upvotes
        context["answers"] = Answers.objects.all()
        context["upvoted"] = upvoted
        return context
    
    
    # context["total_upvotes"] = total_upvotes

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