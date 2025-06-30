from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.http import HttpResponse

from laundryabc_app.models import PaketLaundry
from api.serializers import PaketLaundrySerializer  # ✅ Perbaikan di sini

def homepage_view(request):
    return HttpResponse("Selamat datang di Laundry ABC!")

class PaketLaundryGetPost(ListCreateAPIView):
    queryset = PaketLaundry.objects.all()
    serializer_class = PaketLaundrySerializer

class PaketLaundryGetUpDel(RetrieveUpdateDestroyAPIView):
    queryset = PaketLaundry.objects.all()
    serializer_class = PaketLaundrySerializer
