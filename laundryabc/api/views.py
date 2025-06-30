from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.http import HttpResponse

from laundryabc_app.models import PaketLaundry,KategoriLayanan
from api.serializers import PaketLaundrySerializer, KategoriLayananSerializer

class PaketLaundryGetPost(ListCreateAPIView):
    queryset = PaketLaundry.objects.all()
    serializer_class = PaketLaundrySerializer

class PaketLaundryGetUpDel(RetrieveUpdateDestroyAPIView):
    queryset = PaketLaundry.objects.all()
    serializer_class = PaketLaundrySerializer

class KategoriLayananGetPost(ListCreateAPIView):
    queryset = KategoriLayanan.objects.all()
    serializer_class = KategoriLayananSerializer

class KategoriLayananGetUpDel(RetrieveUpdateDestroyAPIView):
    queryset = KategoriLayanan.objects.all()
    serializer_class = KategoriLayananSerializer