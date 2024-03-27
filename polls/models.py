import datetime
from django.db import models
from django.utils import timezone

'''
The initialization of Django models is handled internally by Django's ORM (Object-Relational Mapping) system, 
and you don't need to define an __init__ method explicitly for model classes. 
however you may use __str__ in the model to ensure instances of a model are represented in human-readable strings
'''
# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    
    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text
    
    

#. In Django, models are used to define the database layout or schema. 
# Each model class represents a database table, and each attribute of the model class represents a database field.
'''
by default, Django automatically creates an 'id' field for each object of  a model (which is a unique identifier for that object)
this id automatically increaments for each new object added to the database
'''