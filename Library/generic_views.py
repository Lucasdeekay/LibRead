from django.views.generic import ListView

from Library.models import Ebook, Journal


class EbookGenericView(ListView):
    model = Ebook
    paginate_by = 12
    context_object_name = 'all_ebooks'
    queryset = Ebook.objects.all().order_by('-date')
    template_name = 'library/offline_resources.html'


class JournalGenericView(ListView):
    model = Journal
    paginate_by = 2
    context_object_name = 'approved_journals'
    queryset = Journal.objects.filter(is_approved=True).order_by('-date')
    template_name = 'library/offline_resources.html'
