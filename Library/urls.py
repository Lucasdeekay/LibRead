from django.urls import path, include

from Library import views

app_name = 'Library'

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('repository', views.library_main, name='library_main'),
]
