from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import IdeaData, SpartanEdu, WebData, EngineeringData, SwData
from .serializers import IdeaSerializer, NoticeSerializer, WebSerializer, EngineeringSerializer, SwSerializer
from django.shortcuts import render

import _spartansw, cron

# Create your views here.

@api_view(['GET'])
def Idea(request):
    totaldata = IdeaData.objects.all()
    serializer = IdeaSerializer(totaldata, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def Web(request):
    totaldata = WebData.objects.all()
    serializer = WebSerializer(totaldata, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def Engineering(request):
    totaldata = EngineeringData.objects.all()
    serializer = EngineeringSerializer(totaldata, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def Sw(request):
    totaldata = SwData.objects.all()
    serializer = SwSerializer(totaldata, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def Spartan(request):
    _spartansw.crawl()
    totaldata = SpartanEdu.objects.all()
    serialzer = NoticeSerializer(totaldata, many = True)
    return Response(serialzer.data)

@api_view(['GET'])
def Crawling(request):
    cron.run()
    return Response("크롤링 완료!")