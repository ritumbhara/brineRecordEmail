from rest_framework import serializers


class EmailDetailSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=200)

    class Meta:
        fields = ("email",)