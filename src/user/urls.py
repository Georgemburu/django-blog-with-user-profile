from django.urls import path
from .views import (
    UserCreationView, 
    UserProfileView
)
from django.contrib.auth.views import (
    LoginView,
    LogoutView
)


urlpatterns = [
     path('create/',UserCreationView.as_view(), name="user_create"),
     path('logout/',LogoutView.as_view(template_name='user/user_logout.html'),name="user_logout"),
     path('login/',LoginView.as_view(template_name='user/user_login.html'),name="user_login"),
     path('user/<int:pk>/profile',UserProfileView,name="user_profile")
]
