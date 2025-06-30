from django.urls import path
from .views import (PaketLaundryGetPost, PaketLaundryGetUpDel,KategoriLayananGetPost,KategoriLayananGetUpDel)

app_name = 'api'

urlpatterns = [
    path('paket', PaketLaundryGetPost.as_view()),            # GET all + POST
    path('paket/<int:pk>', PaketLaundryGetUpDel.as_view()),  # GET single + PUT + DELETE
    path('paket', KategoriLayananGetPost.as_view()),            # GET all + POST
    path('paket/<int:pk>', KategoriLayananGetUpDel.as_view()),  # GET single + PUT + DELETE   
]
