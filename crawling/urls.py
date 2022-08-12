from django.urls import path, include
from django.urls import URLPattern
from .views import Spartan, Idea, Web, Engineering, Sw
from .views import Crawling

urlpatterns = [
    path("idea/", Idea),
    path("web/", Web),
    path("engineering/", Engineering),
    path("sw/", Sw),
    path("spartan/", Spartan),
    path("run_crawling/", Crawling),
]