from django.urls import path, include
from rest_framework import routers

from Blog import views
from Blog.api_views import BlogView, CommentView

app_name = 'Blog'

router = routers.DefaultRouter()
router.register('blog', BlogView)
router.register('comment', CommentView)

urlpatterns = [
    path('', views.home, name='home'),
    path('details/<str:title>', views.blog_page, name='blog_page'),
    path('api/', include(router.urls))
]