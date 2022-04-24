from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from .models import Questions,Answers
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

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

    
    # Remember to give ordering based on the upvotes.

@login_required
def upvoting(request):
    user = request.user
    if request.method == 'POST':
        quest_id = request.POST.get('quest_id')
        quest = get_object_or_404(Questions,id=quest_id)
        print(quest_id)
        print(quest)
        quest.upvotes.add(request.user)
        print("upvote added")
        result = quest.total_upvotes()
        print("Result = ",result)
        quest.save()
        return JsonResponse({'result': result,})
    return redirect('home')

@login_required
def downvoting(request):
    user = request.user
    if request.method == 'POST':
        quest_id = request.POST.get('quest_id')
        quest = get_object_or_404(Questions, id=quest_id)
        print(quest_id)
        print(quest)
        quest.upvotes.remove(request.user)
        quest.save()
        print("upvote removed")
        result = quest.total_upvotes()
        print("Result = ",result)
        return JsonResponse({'result': result,})
    return redirect('home')


class QuestionsDetailView(DetailView):
    model = Questions
    template_name = 'qna.html'
    def get_context_data(self, **kwargs):
        context = super(QuestionsDetailView, self).get_context_data(**kwargs)
        grab = get_object_or_404(Questions, id=self.kwargs['pk'])
        # upvoted = False

        # if grab.upvotes.filter(id = self.request.user.id).exists():
        #     upvoted=True
        total_upvotes = grab.total_upvotes()
        context["total_upvotes"] =  total_upvotes
        context["answers"] = Answers.objects.filter(question_id=grab.id)
        # context["upvoted"] = upvoted
        return context
    
    
    # context["total_upvotes"] = total_upvotes

class QuestionsCreateView(LoginRequiredMixin, CreateView):
    model = Questions
    fields = ['title','content','category','quest_image']
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

def PostAnswers(request):
    if request.method == 'POST':
        userid = request.user.id
        answer = request.POST['answer_content']
        quest_id = request.POST.get('questionid')
        print(answer)
        print("Hello")
        print(quest_id)
        Answers.objects.create(answer = answer,question_id = quest_id,author_id = userid)
        # return redirect('QES:qna')
        return redirect(f'qna/{quest_id}')
    else:
        return render(request, 'qna.html')

# def qna(request):
#     return render(request,'qna.html')

