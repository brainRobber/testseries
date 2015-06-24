from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Userprofile(models.Model):
    user = models.OneToOneField('auth.User', unique=True, related_name='profile')
    role = models.CharField(max_length=50)

    def __unicode__(self):
        return user.__unicode__()

class Test_score(models.Model):
    test_user = models.ForeignKey('Userprofile')
    test_id = models.ForeignKey('Test')
    score = models.DecimalField()

    def __unicode__(self):
        return '%s, %s' % (self.test_user.__unicode__(), self.test_id.__unicode__())

class Breakup(models.Model):
    test_score = models.ForeignKey('Test_score')
    single_choice_score = models.DecimalField()
    multiple_choice_score = models.DecimalField()
    integer_type_score = models.DecimalField()
    list_type_score = models.DecimalField()

    def __unicode__(self):
        return test_score.__unicode__()

class Test(models.Model):
    test_name = models.CharField(max_length=200, unique=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    duration = models.DecimalField(max_digits=5, decimal_places=0)
    syllabus = models.CharField(max_length=200)

    def __unicode__(self):
        return self.test_name

class Single_choice(models.Model):
    test = models.ForeignKey('Test')
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
    test = models.ForeignKey('Test')
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


