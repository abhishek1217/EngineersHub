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

    
def viewprofile(request):
     return render(request, 'view-profile.html')

@login_required
def upvoting(request):
    if request.method == 'POST':
        quest_id = request.POST.get('quest_id')
        quest = get_object_or_404(Questions, id=quest_id)
        print(quest_id)
        user_id = request.user.id
        print(quest.title)
        print("User id= ",user_id)
        if not quest.upvotes.filter(id=user_id).exists():
            if quest.downvoted == 'False':
                quest.upvotes.add(request.user)
                quest.totalvotes += 1
            else:
                quest.upvotes.add(request.user)
                quest.totalvotes += 1
                quest.downvoted = 'False'
            quest.save()
        result = quest.totalvotes
        return JsonResponse({'result' : result,})

@login_required
def downvoting(request):
    if request.method == 'POST':
        quest_id = request.POST.get('q_id')
        quest = get_object_or_404(Questions, id=quest_id)
        print(quest_id)
        print(quest.title)
        user_id = request.user.id
        print("User id= ",user_id)
        if quest.upvotes.filter(id=user_id).exists():
            print('Here')
            quest.upvotes.remove(request.user)
            quest.totalvotes -= 1
            quest.downvoted = 'True'
            quest.save()
        else:
            print('Here 2')
            if quest.downvoted == 'False':
                print('Here 3')
                quest.totalvotes -= 1
                quest.downvoted = 'True'
                quest.save()
        result = quest.totalvotes
        return JsonResponse({'result' : result, })

class QuestionsDetailView(DetailView):
    model = Questions
    template_name = 'qna.html'
    def get_context_data(self, **kwargs):
        context = super(QuestionsDetailView, self).get_context_data(**kwargs)
        grab = get_object_or_404(Questions, id=self.kwargs['pk'])
        # upvoted = False

        # if grab.upvotes.filter(id = self.request.user.id).exists():
        #     upvoted=True
        # total_upvotes = grab.total_upvotes()
        # context["total_upvotes"] =  total_upvotes
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

