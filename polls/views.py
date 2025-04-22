from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Choice
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5] 
    return render(request, 'polls/index.html', {'latest_questions': latest_questions})


# Displays a specific question and its choices
@login_required
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


# Handles user voting
@login_required
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
        return redirect('polls:results', question_id=question.id)


# Shows the voting results
@login_required
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
