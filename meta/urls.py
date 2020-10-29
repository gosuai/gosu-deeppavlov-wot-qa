from django.urls import include, path
from meta import settings


urlpatterns = [
    path(settings.PREFIX, include('homepage.urls')),
]
