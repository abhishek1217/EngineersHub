from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from .models import Questions,Answers
from users.models import Profile
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

class QuestionsListView(ListView):
    model = Questions
    template_name = 'home.html' # <app>/<model>_<viewtype>.html
    context_object_name = "questions"
    ordering = ['-date_posted']
    def get_context_data(self, **kwargs):
        context = super(QuestionsListView, self).get_context_data()
        context['profiles'] = Profile.objects.all().order_by('-reputation')[:7]
        return context

def about(request):
    return render(request,'about.html')

def viewprofile(request):
    user_id = request.user.id
    questions = Questions.objects.all().filter(author_id=user_id)
    profile = get_object_or_404(Profile, id=user_id)
    context = {
        'questions' : questions,
        'profile' : profile
    }
    return render(request, 'viewprofile.html',context)

@login_required
def upvoting(request):
    if request.method == 'POST':
        quest_id = request.POST.get('quest_id')
        quest = get_object_or_404(Questions, id=quest_id)
        user_id = request.user.id
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
def upvotingans(request):
    if request.method == 'POST':
        ans_id = request.POST.get('ans_id')
        answer = get_object_or_404(Answers, id=ans_id)
        user_id = request.user.id
        if not answer.ans_upvotes.filter(id=user_id).exists():
            if answer.downvoted == 'False':
                answer.ans_upvotes.add(request.user)
                answer.totalvotes += 1
            else:
                answer.ans_upvotes.add(request.user)
                answer.totalvotes += 1
                answer.downvoted = 'False'
            answer.save()
        result = answer.totalvotes
        return JsonResponse({'result' : result,})


@login_required
def downvoting(request):
    if request.method == 'POST':
        quest_id = request.POST.get('q_id')
        quest = get_object_or_404(Questions, id=quest_id)
        user_id = request.user.id
        if quest.upvotes.filter(id=user_id).exists():
            quest.upvotes.remove(request.user)
            quest.totalvotes -= 1
            quest.downvoted = 'True'
            quest.save()
        else:
            if quest.downvoted == 'False':
                quest.totalvotes -= 1
                quest.downvoted = 'True'
                quest.save()
        result = quest.totalvotes
        return JsonResponse({'result' : result, })

@login_required
def downvotingans(request):
    if request.method == 'POST':
        ans_id = request.POST.get('a_id')
        answer = get_object_or_404(Answers, id=ans_id)
        user_id = request.user.id
        if answer.ans_upvotes.filter(id=user_id).exists():
            answer.ans_upvotes.remove(request.user)
            answer.totalvotes -= 1
            answer.downvoted = 'True'
            answer.save()
        else:
            if answer.downvoted == 'False':
                answer.totalvotes -= 1
                answer.downvoted = 'True'
                answer.save()
        result = answer.totalvotes
        return JsonResponse({'result' : result, })

class QuestionsDetailView(DetailView):
    model = Questions
    template_name = 'qna.html'
    def get_context_data(self, **kwargs):
        context = super(QuestionsDetailView, self).get_context_data(**kwargs)
        grab = get_object_or_404(Questions, id=self.kwargs['pk'])
        context["answers"] = Answers.objects.filter(question_id=grab.id).order_by('-totalvotes')
        context['profiles'] = Profile.objects.all().order_by('-reputation')[:7]
        return context
    

class QuestionsCreateView(LoginRequiredMixin, CreateView):
    model = Questions
    fields = ['title','content','category']
    template_name = 'add_question.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class QuestionsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Questions
    fields = ['title','content','category','quest_image']
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
        Answers.objects.create(answer = answer,question_id = quest_id,author_id = userid)
        return redirect(f'qna/{quest_id}')
    else:
        return render(request, 'qna.html')

