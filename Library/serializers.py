from rest_framework import serializers

from Library.models import Clientele, Password, Ebook


class ClienteleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientele
        field = '__all__'


class PasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Password
        field = '__all__'


class EbookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ebook
        field = '__all__'
