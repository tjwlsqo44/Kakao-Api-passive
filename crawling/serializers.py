from dataclasses import Field, fields
from rest_framework import serializers
from .models import SpartanEdu, SwData, WebData, IdeaData, EngineeringData

class IdeaSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdeaData
        fields =('title', 'due', 'link')

class WebSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebData
        fields = ('title', 'due', 'link')

class EngineeringSerializer(serializers.ModelSerializer):
    class Meta:
        model = EngineeringData
        fields = ('title', 'due', 'link')

class SwSerializer(serializers.ModelSerializer):
    class Meta:
        model = SwData
        fields = ('title', 'due', 'link')

class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpartanEdu
        fields = ('title', 'link')