from django.urls import path, include
from rest_framework import routers

from Blog import views
from Blog.api_views import BlogView

app_name = 'Blog'

router = routers.DefaultRouter()
router.register('blog', BlogView)

urlpatterns = [
    path('', views.home, name='home'),
    path('api/', include(router.urls))
]