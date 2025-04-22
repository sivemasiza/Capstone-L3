from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Choice
from django.contrib.auth.decorators import login_required

"""
This module contains the views for the polls application.
The views handle displaying questions, voting on choices, and showing voting results.
Each view is restricted to authenticated users via the @login_required decorator.
"""

@login_required
def index(request):
    """
    View function to display the latest questions.
    
    This function retrieves the five most recent questions from the database and renders them
    on the 'polls/index.html' template.
    """
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    return render(request, 'polls/index.html', {'latest_questions': latest_questions})


@login_required
def detail(request, question_id):
    """
    View function to display a specific question and its choices.
    
    This function retrieves the question identified by 'question_id' from the database
    and renders it on the 'polls/detail.html' template. If the question is not found, a 404 error
    will be raised.
    
    Args:
        question_id (int): The ID of the question to be displayed.
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


@login_required
def vote(request, question_id):
    """
    View function to handle user voting on a specific question.
    
    This function processes the user's vote for the question identified by 'question_id'.
    It retrieves the selected choice from the request data, increments its vote count,
    and saves the updated choice. If no choice is selected or an invalid choice is provided, 
    an error message is displayed.
    
    Args:
        question_id (int): The ID of the question being voted on.
    """
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


@login_required
def results(request, question_id):
    """
    View function to display the voting results for a specific question.
    
    This function retrieves the voting results for the question identified by 'question_id'
    and renders them on the 'polls/results.html' template.
    
    Args:
        question_id (int): The ID of the question for which the results are to be displayed.
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
