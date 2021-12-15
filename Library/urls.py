from django.urls import path, include

from Library import views

app_name = 'Library'

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('login', views.login, name='login'),
    path('login/forgot-password', views.forgotten_password, name='forgot_password'),
    path('login/forgot-password/retrieve-password', views.password_retrieval, name='password_retrieval'),
    path('login/forgot-password/retrieve-password/update', views.update_password, name='update_password'),
    path('register', views.register, name='register'),
    path('repository', views.repository, name='repository'),
    path('repository/e-books', views.offline_resources, name='offline_resources'),
]
