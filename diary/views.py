from django.shortcuts import render
from diary.models import Tag, Page, Diary
from django.views import generic

# def index(request):
#     num_pages = Page.objects.all()
#     num_tags = Tag.objects.all()
#     num_diarys = Diary.objects.all()
    
#     context = {
#         'num_diarys': num_diarys,
#         'num_pages': num_pages,
#         'num_tags': num_tags,
#     }

#     # Render the HTML template index.html with the data in the context variable
#     return render(request, 'index.html', context=context)

class IndexView(generic.ListView):
    template_name = 'diary/index.html'
    context_object_name = 'all_diarys'

    def get_queryset(self):
        """
        Return all of the objects in the list
        """
        return Diary.objects.all()
