from rest_framework import viewsets

from Library.models import Clientele, Password, Ebook, Journal
from Library.serializers import ClienteleSerializer, PasswordSerializer, EbookSerializer, JournalSerializer


class ClienteleView(viewsets.ModelViewSet):
    serializer_class = ClienteleSerializer
    queryset = Clientele.objects.all()


class PasswordView(viewsets.ModelViewSet):
    serializer_class = PasswordSerializer
    queryset = Password.objects.all()


class EbookView(viewsets.ModelViewSet):
    serializer_class = EbookSerializer
    queryset = Ebook.objects.all()


class JournalView(viewsets.ModelViewSet):
    serializer_class = JournalSerializer
    queryset = Journal.objects.all()
