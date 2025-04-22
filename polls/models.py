from django.db import models

"""
This module contains the models for the polls application.
The models define two key entities: Question and Choice, representing the poll questions 
and the available choices for each question, respectively.

Fields:
    - Question:
        - question_text (CharField): The text of the poll question (max length 200 characters).
        - pub_date (DateTimeField): The date and time when the poll question was published.

    - Choice:
        - question (ForeignKey): A link to the Question model, indicating which question this choice belongs to.
        - choice_text (CharField): The text of the choice (max length 200 characters).
        - votes (IntegerField): The number of votes this choice has received (defaults to 0).
"""


class Question(models.Model):
    """
    Model that represents a poll question.
    
    A Question has text describing the question and a publication date.
    
    Fields:
        - question_text (CharField): The text of the poll question (max length 200 characters).
        - pub_date (DateTimeField): The date and time when the poll question was published.
    
    Methods:
        __str__: Returns the question text as its string representation.
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        """
        String representation of the Question model.
        
        Returns:
            str: The text of the poll question.
        """
        return self.question_text


class Choice(models.Model):
    """
    Model that represents a choice for a specific poll question.
    
    A Choice is linked to a Question and has associated text and a vote count.
    
    Fields:
        - question (ForeignKey): A link to the Question model, indicating which question this choice belongs to.
        - choice_text (CharField): The text of the choice (max length 200 characters).
        - votes (IntegerField): The number of votes this choice has received (defaults to 0).
    
    Methods:
        __str__: Returns the choice text as its string representation.
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        """
        String representation of the Choice model.
        
        Returns:
            str: The text of the choice.
        """
        return self.choice_text
