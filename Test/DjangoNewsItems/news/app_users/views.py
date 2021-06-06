import time

from .forms import AuthForm
from django.contrib.auth.views import LoginView,LogoutView


class UserLoginView(LoginView):
    template_name = 'users/login.html'


class UserLogoutView(LogoutView):
    template_name = 'users/logout.html'




