from django.shortcuts import render

from Library.models import Clientele


def home(request):
    context = {}
    if request.user.is_authenticated and not request.user.is_superuser:
        current_clientele = Clientele.objects.get(clientele_id=request.user.username)
        context = {'current_clientele': current_clientele}
    return render(request, 'blog/home.html', context)


