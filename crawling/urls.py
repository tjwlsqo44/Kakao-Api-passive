from django.urls import path, include
from django.urls import URLPattern
from .views import Spartan, testAPI, Idea, Web, Engineering, Sw

urlpatterns = [
    path("test/", testAPI),
    path("idea/", Idea),
    path("web/", Web),
    path("engineering/", Engineering),
    path("sw/", Sw),
    path("spartan/", Spartan),
]