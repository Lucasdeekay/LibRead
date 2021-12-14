from django.urls import path, include

from Library import views

app_name = 'Library'

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact')
]