from django.db import models

# Create your models here.
class Survey(models.Model):
    title = models.CharField(max_length = 300)

class Question(models.Model):
    question_text = models.CharField(max_length = 900)
    survey = models.ForiegnKey(Survey)

class Choice(models.Model):
    choice_text = models.CharField(max_length = 900)
    question = models.ForiegnKey(Question)

class SurveyAnswer(models.Model):
    orig_survey = models.ForiegnKey(Survey)

class QuestionAnswer(models.Model):
    answer = models.ForiegnKey(Choice)
    survey_answer = models.ForiegnKey(Survey)
