from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from .models import Question, Choice


class IndexView(LoginRequiredMixin, generic.ListView):
    login_url = '/login/'
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(LoginRequiredMixin, generic.DetailView):
    login_url = '/login/'
    model = Question
    template_name = 'polls/detail.html'

#For admin only
class ResultsView(LoginRequiredMixin, generic.DetailView):
    login_url = '/login/'
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        messages.info(request, 'Thank you for your vote!')
        return HttpResponseRedirect(reverse('polls:index'))
