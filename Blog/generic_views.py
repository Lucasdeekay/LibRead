from django.views.generic import ListView

from Blog.models import Blog


class BlogGenericView(ListView):
    model = Blog
    paginate_by = 5
    context_object_name = 'all_blogs'
    queryset = Blog.objects.all().order_by('-date')
    template_name = 'blog/home.html'
