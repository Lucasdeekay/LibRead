from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone

from Blog.models import Blog, Comment
from Library.forms import CommentForm
from Library.models import Clientele


def home(request):
    all_blogs = Blog.objects.all().order_by('-date')
    paginator = Paginator(all_blogs, 5)  # Show 5 blogs per page.

    page_number = request.GET.get('page')  # Get each paginated pages
    blog_obj = paginator.get_page(page_number)  # Insert the number of items into page

    if request.user.is_authenticated and not request.user.is_superuser:
        current_clientele = Clientele.objects.get(clientele_id=request.user.username)
        context = {'current_clientele': current_clientele, 'all_blogs': all_blogs, 'blog_obj': blog_obj}
        return render(request, 'blog/home.html', context)
    else:
        context = {'all_blogs': all_blogs, 'blog_obj': blog_obj}
        return render(request, 'blog/home.html', context)


def blog_page(request, title):
    blog = get_object_or_404(Blog, title=title)
    comments = Comment.objects.filter(blog=blog)

    if request.user.is_authenticated and not request.user.is_superuser:
        current_clientele = Clientele.objects.get(clientele_id=request.user.username)
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.cleaned_data['comment'].strip()
                Comment.objects.create(blog=blog, clientele=current_clientele, comment=comment, date=timezone.now())
                return HttpResponseRedirect(reverse('Blog:blog_page', args=(title,)))
        else:
            form = CommentForm()
            context = {'blog': blog, 'comments': comments, 'form': form, 'current_clientele': current_clientele}
            return render(request, 'blog/blog_page.html', context)
    else:
        messages.error(request, 'Please login to have access')
        return HttpResponseRedirect(reverse('Library:login'))


