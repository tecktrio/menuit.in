
from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include
from rest_framework.response import Response
from rest_framework.views import APIView

from django.conf import settings
from django.conf.urls.static import static

def HomePage(request):
    return render(request, 'index.html')


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', HomePage),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

