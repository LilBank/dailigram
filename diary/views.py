from diary.models import Tag, Page, Diary
from django.views import generic, View
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .forms import UserForm, PageForm
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse
from django.urls import reverse_lazy
from utility.imgur import ImgurUtil

from django import forms

import requests
import datetime


def login_user(request):
    """
    If the user is not authenticated, get user's request and execute login. 
    """
    if not request.user.is_authenticated:
        form = UserForm(request.POST or None)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                HttpResponseRedirect(reverse('diary:index'))
            else:
                return render(request, 'registration/login.html', {'form': form})
        else:
            return render(request, 'registration/login.html', {'form': form})
    return HttpResponseRedirect(reverse('diary:index'))


def logout_user(request):
    """
    Function to logout user and redirect to login page. 
    """
    logout(request)
    return HttpResponseRedirect('/login')


class IndexView(generic.ListView):
    template_name = 'diary/index.html'
    context_object_name = 'all_pages'

    def get_queryset(self):
        """
        Return all of the objects in the list of diary.
        """
        username = self.request.user.username
        diaries = Diary.objects.filter(username=username)
        imgurUtil = ImgurUtil()

        if len(diaries) == 0:
            Diary.objects.create(username=username)

        if(imgurUtil.get_album_hash(username) is None):
            imgurUtil.create_album(username)

        return Page.objects.filter(diary__username=username)


class DetailView(generic.DetailView):
    model = Page
    template_name = 'diary/detail.html'

class CreateSettings(View):
    template_name = 'diary/settings.html'

    def get(self, request):
        return render(request, self.template_name)

class CreateFormat(View):
    template_name = 'diary/format.html'

    def get(self, request):
        return render(request, self.template_name)


class CreatePage(View):
    form_class = PageForm
    template_name = 'diary/page_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid() and request.FILES['myfile']:
            username = self.request.user.username
            page = form.save(commit=False)
            page.date = str(datetime.date.today())
            diary = Diary.objects.filter(username=username)
            page.diary = diary[0]
            imgurUtil = ImgurUtil()
            my_file = request.FILES['myfile']
            description = page.title + ':' + page.date
            hashes = imgurUtil.get_album_hash(username)
            imgurUtil.set_album_hash(hashes)
            response = imgurUtil.upload_image_locally(description, my_file)
            if(response.status_code == requests.codes.ok):
                uploader_url = response.json()["data"]["link"]
                page.picture = uploader_url
                page.save()
        return HttpResponseRedirect("/diary/")


class DeleteDiary(DeleteView):
    form_class = PageForm
    model = Page
    success_url = reverse_lazy('diary:index')
 
    def delete(self, request, *args, **kwargs):
        """
        Function to delete picture from database and imgur.
        """
        imgurUtil = ImgurUtil()
        page = self.get_object()
        description = page.title + ':' + page.date
        username = self.request.user.username
        hashes = imgurUtil.get_album_hash(username)
        imgurUtil.set_album_hash(hashes)
        image_hash = imgurUtil.get_image_hash(description)
        imgurUtil.delete_image(image_hash)
        page.delete()
        return HttpResponseRedirect('/diary/')


class UserFormView(View):
    form_class = UserForm
    template_name = 'registration/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/login')

        return render(request, self.template_name, {'form': form})