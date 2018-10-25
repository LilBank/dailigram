from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import datetime

class Tag(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a tag (e.g. Love, Happy, Sad)')
    
    def __str__(self):
        return self.name

class Page(models.Model):
    diary = models.ForeignKey('Diary', on_delete=models.SET_NULL, null=True)  
    tag = models.ForeignKey('Tag', on_delete=models.SET_NULL, null=True) 
    story = models.CharField(max_length=1000, help_text='Write your story.')
    # date = datetime.date.today()
    date = models.DateField('Date')
    def __str__(self):
        return f'{str(self.date)}, {self.diary}, {self.tag}'
    
    def get_absolute_url(self):
        return reverse('diary-detail', args=[str(self.id)])

class Diary(models.Model):
    first_name = models.CharField(max_length=100,unique=True)
    
    def get_absolute_url(self):
        return reverse('user-detail', args=[str(self.id)])

    def __str__(self):
        return self.first_name