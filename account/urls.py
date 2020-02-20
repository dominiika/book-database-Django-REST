from django.contrib.auth.views import LoginView, LogoutView
from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^signup/$', views.signup, name='signup'),
    re_path(r'^login/$', LoginView.as_view(template_name='account/login.html'), name='login'),
    re_path(r'^logout/$', LogoutView.as_view(), name='logout'),
]
