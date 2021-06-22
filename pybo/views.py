from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from django.http import HttpResponse


class Index(APIView):
    def get(self, request):
        return HttpResponse("Hello, Django!")
