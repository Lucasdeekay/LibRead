from django.shortcuts import render

from Blog.models import Blog
from Library.models import Clientele


def home(request):
    context = {}
    if request.user.is_authenticated and not request.user.is_superuser:
        current_clientele = Clientele.objects.get(clientele_id=request.user.username)
        all_blogs = Blog.objects.all()
        context = {'current_clientele': current_clientele, 'all_blogs': all_blogs}
    return render(request, 'blog/home.html', context)
