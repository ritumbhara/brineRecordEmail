import traceback

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import EmailDetailSerializer
from .models import EmailDetail, EmailDetail
from django.http import JsonResponse


class EmailItemViews(APIView):

    def post(self, request):
        try:
            serializer = EmailDetailSerializer(data=request.data)
            if serializer.is_valid() is False:
                return Response(data={
                    "status": "error",
                    "data": serializer.errors},
                    status=status.HTTP_400_BAD_REQUEST
                )

            validated_data = serializer.validated_data
            email = validated_data.get("email")

            email_detail = EmailDetail.objects.create(email=email)
            return Response(data={
                "status": "success",
                "data": {}},
                status=status.HTTP_200_OK)
        except Exception:
            print(traceback.format_exc())

