from __future__ import unicode_literals
from diary.models import Tag, Page, Diary
from django.views import generic, View
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .forms import UserForm, ImageUrlForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView
from django.urls import reverse
from utility.imgur import ImgurUtil

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


class CreateFormat(View):
    template_name = 'diary/format.html'

    def get(self, request):
        return render(request, self.template_name)


class CreateDiary(View):
    form_class = ImageUrlForm
    template_name = 'diary/page_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid() and request.FILES['myfile']:
            imgur = ImgurUtil()
            myfile = request.FILES['myfile']
            response = imgur.upload_image_locally('', myfile)
            if(response.status_code == requests.codes.ok):
                uploader_url = response.json()["data"]["link"]
                return render(request, 'diary/page_form.html', {'uploaded_file_url': uploader_url})
            else:
                print('need to fix')
        return render(request, self.template_name, {'form': form})

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
