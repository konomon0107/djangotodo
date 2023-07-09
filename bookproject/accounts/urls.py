from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import signup,login_view

app_name = 'accounts'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', signup, name='signup'),
]
