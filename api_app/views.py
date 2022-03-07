from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import EmailItemSerializer
from .models import EmailItem
from django.http import JsonResponse

class EmailItemViews(APIView):
    def post(self, request):
        serializer = EmailItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request):
        items_count = EmailItem.objects.count()
        items = EmailItem.objects.all()

        items_data = []
        for item in items:
            items_data.append({
                'email': item.email,
            })

        data = {
            'items': items_data,
            'count': items_count,
        }

        return JsonResponse(data)