from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Test(models.Model):
    test_name = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    duration = models.DecimalField(max_digits=5, decimal_places=0)
    syllabus = models.CharField(max_length=200)

    def __unicode__(self):
        return self.test_name

class Single_choice(models.Model):
    test_id = models.ForeignKey('Test')
    question_text = models.CharField(max_length=500)
    choice_a = models.CharField(max_length=200)
    choice_b = models.CharField(max_length=200)
    choice_c = models.CharField(max_length=200)
    choice_d = models.CharField(max_length=200)
    solution = models.CharField(max_length=10, default='A', choices=(
        ('a','A'),
        ('b','B'),
        ('c','C'),
        ('d','D'),))

    def __unicode__(self):
        return self.question_text

class Multiple_choice(models.Model):
    test_id = models.ForeignKey('Test')
    question_text = models.CharField(max_length=500)
    choice_a = models.CharField(max_length=200)
    choice_b = models.CharField(max_length=200)
    choice_c = models.CharField(max_length=200)
    choice_d = models.CharField(max_length=200)

    def __unicode__(self):
        return self.question_text


class Choice(models.Model):
    test_id = models.ForeignKey('Multiple_choice')
    solution = models.CharField(max_length=10, choices=(
        ('a','A'),
        ('b','B'),
        ('c','C'),
        ('d','D'),))

    def __unicode__(self):
        return self.solution


