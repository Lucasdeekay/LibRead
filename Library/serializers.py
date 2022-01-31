from rest_framework import serializers
from Library.models import Clientele, Password, Ebook, Journal


class ClienteleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientele
        fields = "__all__"


class PasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Password
        fields = "__all__"


class EbookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ebook
        fields = "__all__"


class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = "__all__"