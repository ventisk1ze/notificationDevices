from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Device


class DeviceView(APIView):
    def get(self, request):
        devices = Device.objects.all()
        return Response({"devices":devices})
    
