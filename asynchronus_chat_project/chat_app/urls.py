from base64 import urlsafe_b64decode
from urllib.parse import urlparse
from django.urls import path
from . import views
urlpatterns = [
    path('',views.homepage,name="homepage")
]
