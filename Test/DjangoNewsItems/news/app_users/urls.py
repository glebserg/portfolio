from django.urls import path
from .views import UserLoginView,UserLogoutView

urlpatterns = [
    path('users/login/', UserLoginView.as_view(), name='login'),
    path('users/logout/', UserLogoutView.as_view(), name='logout'),
]
