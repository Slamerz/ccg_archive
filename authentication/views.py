from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from authentication.forms import RegisterUserForm


class LoginUserView(LoginView):
    """
    A View that allows the user to log into their account
    """

    template_name = 'generic-form.html'
    extra_context = {'allow_register': True}


@method_decorator(login_required, name='dispatch')
class LogoutUserView(LogoutView):
    """
    A View that Signs the user out and redirects them to the homepage
    """

    next_page = '/'


class RegisterUserView(CreateView):
    """
    A view to register as a user of the website
    """

    template_name = 'generic-form.html'
    form_class = RegisterUserForm

    def form_valid(self, form):
        data = form.cleaned_data
        user = User.objects.create_user(
            username=data['username'],
            email=data['email'],
            password=data['password'],
            first_name=data['first_name'],
            last_name=data['last_name']
        )
        login(self.request, user)
        return HttpResponseRedirect(reverse_lazy('homepage'))
