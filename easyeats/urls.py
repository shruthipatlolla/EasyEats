# easyeats/urls.py
from django.conf.urls import url

from . import views
from views import AboutPageView, ContactPageView, MenuPAgeView, ProfilePageView, emailView, successView


urlpatterns = [
    url('signup/', views.SignUp.as_view(), name='signup'),
    url('about/',  AboutPageView.as_view(), name='about'),
    url('contact/',  ContactPageView.as_view(), name='contact'),
    #url('menu/',  MenuPAgeView.as_view(), name='menu'),
    url('profile/',  ProfilePageView.as_view(), name='profile'),
    url('email/', emailView, name='email'),
    url('success/', successView, name='success'),
]