from diary.models import Tag, Page, Diary
from django.views import generic, View
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .forms import UserForm, PageForm, ProfileForm
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from django.urls import reverse_lazy
from utility.imgur import ImgurUtil
from django.db.models import Q
from django import forms
import requests
import datetime


def login_user(request):
    """
    If the user is not authenticated, get user's request and execute login.
    """
    if not request.user.is_authenticated:
        form = UserForm(request.POST or None)
        if request.method == "POST":
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
                messages.error(request, 'username or password is not correct')
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
        Get the queryset to look an object up against.
        """
        username = self.request.user.username
        diaries = Diary.objects.filter(username=username)
        page = Page.objects.all()
        imgurUtil = ImgurUtil()

        query = self.request.GET.get("q")

        if query:
            return page.filter(
                Q(title__icontains=query)
            ).distinct()

        if len(diaries) == 0:
            Diary.objects.create(username=username)

        hashes = '9DACERm'
        imgurUtil.set_album_hash(hashes)

        return Page.objects.filter(diary__username=username)


class DetailView(generic.DetailView):
    model = Page
    template_name = 'diary/detail.html'
    queryset = Page.objects.all()

    def get_queryset(self):
        """
        Get the queryset to look an object up against. This will only display the specific diary's username.
        """
        username = self.request.user.username
        return Page.objects.filter(diary__username=username)


class Settings(UpdateView):
    form_class = ProfileForm
    template_name = 'diary/settings.html'
    success_url = reverse_lazy('diary:index')

    def get_object(self, queryset=None):
        """
        Returns the object the view is displaying.
        """
        return self.request.user


class Format(View):
    template_name = 'diary/format.html'

    def get(self, request):
        return render(request, self.template_name)


class CreatePage(View):
    form_class = PageForm
    template_name = 'diary/create_page.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            try:
                request.FILES['myfile']
            except:
                messages.error(
                    request, 'Please select a file.')
                return HttpResponseRedirect("/diary/create_page")

            error = self.__check_title(form)

            if (error is not None):
                messages.error(request, error)
                return HttpResponseRedirect("/diary/create_page")

            page = form.save()
            imgurUtil = ImgurUtil()
            my_file = request.FILES['myfile']
            username = self.request.user.username
            diary = Diary.objects.filter(username=username)
            page.date = str(datetime.date.today())
            page.diary = diary[0]
            description = str(page.diary) + ':' + \
                str(page.id) + ':' + page.date
            response = imgurUtil.upload_image_locally(description, my_file)
            if(response.status_code == requests.codes.ok):
                uploader_url = response.json()["data"]["link"]
                page.picture = uploader_url
                page.save()

            else:
                messages.error(
                    request, 'Please select a valid file.')
                return HttpResponseRedirect("/diary/create_page")
        return HttpResponseRedirect("/diary/")

    def __check_title(self, form):
        for page in Page.objects.all():
            if page.title == form.cleaned_data.get("title"):
                return 'You already used this title. Please try another one.'


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
        description = str(page.diary) + ':' + str(page.id) + ':' + page.date
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
