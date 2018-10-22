from django.shortcuts import render
from diary.models import Tag, Page, Diary

def index(request):
    num_pages = Page.objects.all().count()
    num_tags = Tag.objects.count()   
    num_diarys = Diary.objects.count()
    
    context = {
        'num_diarys':  num_diarys,
        'num_pages': num_pages,
        'num_tags': num_tags,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
