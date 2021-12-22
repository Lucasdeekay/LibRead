from django.core.paginator import Paginator
from django.shortcuts import render

from Blog.models import Blog
from Library.models import Clientele


def home(request):
    all_blogs = Blog.objects.all().order_by('-date')
    paginator = Paginator(all_blogs, 2)  # Show 5 blogs per page.

    page_number = request.GET.get('page')  # Get each paginated pages
    blog_obj = paginator.get_page(page_number)  # Insert the number of items into page

    if request.user.is_authenticated and not request.user.is_superuser:
        current_clientele = Clientele.objects.get(clientele_id=request.user.username)
        context = {'current_clientele': current_clientele, 'all_blogs': all_blogs, 'blog_obj': blog_obj}
        return render(request, 'blog/home.html', context)
    else:
        context = {'all_blogs': all_blogs, 'blog_obj': blog_obj}
        return render(request, 'blog/home.html', context)



