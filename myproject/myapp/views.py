from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers


def top_page(request):
    return render(request, 'top_page.html')


@login_required
def secret_page(request):
    return render(request, 'secret_page.html')


class AddView(APIView):
    def post(self, request):
        serializer = serializers.AddParamSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            result = self._add(validated_data['value1'], validated_data['value2'])
            return Response(dict(result=result))
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def _add(self, value1, value2):
        return value1 + value2
