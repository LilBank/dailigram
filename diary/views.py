from django.shortcuts import render
from diary.models import Tag, Page, Diary
from django.views.generic import View
from django.views import generic
from django.views.generic.edit import UpdateView, DeleteView
from .forms import UserForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from social_django.models import UserSocialAuth
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

class IndexView(generic.ListView):
    template_name = 'diary/index.html'
    context_object_name = 'all_diarys'
 
    def get_queryset(self):
        """
        Return all of the objects in the list
        """
        return Page.objects.all()

class LoginView(generic.DetailView):
    def post(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/diary')

        return render(request, 'registration/login.html')

def LogoutView(request):
    # user = request.user

    # try:
    #     google_login = user.social_auth.get(provider='google')
    # except UserSocialAuth.DoesNotExist:
    #     google_login = None
    # try:
    #     github_login = user.social_auth.get(provider='github')
    # except UserSocialAuth.DoesNotExist:
    #     github_login = None

    # can_disconnect = (user.social_auth.count() >
    #                   1 or user.has_usable_password())

    # return render(request, 'registration/logout.html', {
    #     'github_login': github_login,
    #     'google_login': google_login,
    #     'can_disconnect': can_disconnect
    # })
    if request.user.is_authenticated:
        if request.user.social_auth.get(provider='google'):
             return render(request, 'registration/login.html')

    return HttpResponseRedirect('/diary')


@login_required
def create(request):
    return render(request, 'registration/create.html')


#  class UserFormView(View):
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
