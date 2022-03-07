from rest_framework import serializers
from .models import EmailItem

class EmailItemSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=200)

    class Meta:
        model = EmailItem
        fields = ('__all__')