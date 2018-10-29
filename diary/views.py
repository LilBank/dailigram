from django.shortcuts import render
from diary.models import Tag, Page, Diary
from django.views import generic
from django.views.generic import View
from django.views.generic.edit import UpdateView, DeleteView
from .forms import UserForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from social_django.models import UserSocialAuth
# from django.contrib.auth.decorators import login_required

# @login_required
class IndexView(generic.ListView):
    template_name = 'diary/index.html'
    context_object_name = 'all_diarys'

    def get_queryset(self):
        """
        Return all of the objects in the list
        """
        return Page.objects.all()

# @login_required
class CreateView(generic.ListView):
    model = Diary
    template_name = 'diary/create.html'

class LoginView(generic.ListView):
    model = Diary
    template_name = 'registration/login.html'

class UserFormView(View):
    form_class = UserForm
    template_name = 'diary/registration_form.html'

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
                    return redirect('diary:index')

        return render(request, self.template_name, {'form': form})

# @login_required
class SettingsView(View):

    def settings(self ,request):

        user = request.user

        try:
            google_login = user.social_auth.get(provider='google')
        except UserSocialAuth.DoesNotExist:
            github_login = None
        try:
            github_login = user.social_auth.get(provider='github')
        except UserSocialAuth.DoesNotExist:
            github_login = None


        can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

        return render(request, 'registration/settings.html', {
            'github_login': github_login,
            'google_login': google_login,
            'can_disconnect': can_disconnect
        })
