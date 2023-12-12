from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from accounts.forms import UserLoginForm
from accounts.views import edit_profile

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html',authentication_form=UserLoginForm),name='login'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'),name='logout'),
    path('profile/', views.view_profile,name='view_profile'),
    path('profile/edit/', views.edit_profile ,name='edit_profile'),
    path('people/', views.view_people ,name='view_people'),
    ]