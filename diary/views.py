from django.shortcuts import render
from diary.models import Tag, Page, Diary
from django.views.generic import View
from django.views.generic.edit import UpdateView, DeleteView
from .forms import UserForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


@login_required
def index(request):
    return render(request, 'diary/index.html')


def LoginView(request):
    if request.user.is_authenticated:

        return HttpResponseRedirect('/diary')

    return render(request, 'registration/login.html')


@login_required
def create(request):
    return render(request, 'diary/create.html')

# class UserFormView(View):
#     form_class = UserForm
#     template_name = 'diary/registration_form.html'

#     # display black form
#     def get(self, request):
#         form = self.form_class(None)
#         return render(request, self.template_name, {'form': form})

#     # process form data
#     def post(self, request):
#         form = self.form_class(request.POST)

#         if form.is_valid():
#             user = form.save(commit=False)

#             # cleaned data
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user.set_password(password)
#             user.save()

#             # return User objects if credential are correct
#             user = authenticate(username=username, password=password)

#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return redirect('diary:index')

#         return render(request, self.template_name, {'form': form})
