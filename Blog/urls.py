from django.urls import path, include

from Blog import views

app_name = 'Blog'

urlpatterns = [
    path('', views.home, name='home'),
]