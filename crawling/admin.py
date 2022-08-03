from django.contrib import admin
from .models import IdeaData, WebData, EngineeringData, SwData

# Register your models here.
admin.site.register(IdeaData)
admin.site.register(WebData)
admin.site.register(EngineeringData)
admin.site.register(SwData)