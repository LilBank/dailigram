from diary.models import Tag, Page, Diary
from django.views import generic, View
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .forms import UserForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView
from django.urls import reverse
from __future__ import unicode_literals
import requests



class IndexView(generic.ListView):
    template_name = 'diary/index.html'
    context_object_name = 'all_diarys'

    def get_queryset(self):
        """
        Return all of the objects in the list
        """
        return Page.objects.all()

class DetailView(generic.DetailView):
    model = Page
    template_name = 'diary/detail.html'

class CreateDiary(CreateView):
    model = Page
    fields = ['diary', 'tag', 'story', 'date', 'picture']

def create_diary(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        url = "https://api.imgur.com/3/image"
        files = { "image": myfile }
        body = { "album": "tC0ylGd" }
        headers = { "Authorization": "Bearer 170f2bf675de202ccb0b26bc25311d0f41a1d84e"}
        r = requests.post(url, files=files, headers=headers, data=body)
        if(r.status_code == requests.codes.ok):
            uploader_url = r.json()["data"]["link"]
            return render(request, 'uploader/index.html', { 'uploaded_file_url': uploader_url})
    return render(request, 'uploader/index.html')

class CreateFormat(View):
    template_name = 'diary/format.html'

    def get(self, request):
        return render(request, self.template_name)
        

class UserFormView(View):
    form_class = UserForm
    template_name = 'registration/registration_form.html'

    # display black form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # cleaned data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # return User objects if credential are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('')

        return render(request, self.template_name, {'form': form})
