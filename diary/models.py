from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import admin
from taggit.managers import TaggableManager

class Tag(models.Model):
    # name = models.CharField(max_length=200, help_text='Enter a tag (e.g. Love, Happy, Sad)')
    content_object = models.ForeignKey('Page')
    
    def __str__(self):
        return self.name

class Page(models.Model):
    diary = models.ForeignKey('Diary', on_delete=models.SET_NULL, null=True)  
    story = models.CharField(max_length=1000, help_text='Write your story.')
    tags = TaggableManager(through=Tag)
    # date = datetime.date.today()
    date = models.DateField('Date')

    def __str__(self):
        return f'{str(self.date)} | {self.diary} | {self.tags}'

class Diary(models.Model):
    first_name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.first_name

class PageAdmin(admin.ModelAdmin):
    list_display = ['tag_list']

    def get_queryset(self, request):
        return super(PageAdmin, self).get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())
