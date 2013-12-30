from django.db import models
from django.contrib.auth.models import User

class User (User):
    presentation = models.CharField(max_length=2000, blank = True)
    
class Conversation (models.Model):
    title = models.CharField(max_length=20)
    participants = models.ManyToManyField(User)
    
class PrivateMessage (models.Model):
    conversation = models.ForeignKey(Conversation)
    content = models.CharField(max_length=2000)
    pub_date = models.DateTimeField('date published')
    
    
