from rest_framework import serializers
from laundryabc_app.models import PaketLaundry, KategoriLayanan

class PaketLaundrySerializer(serializers.ModelSerializer):
    class Meta:
        model = PaketLaundry
        fields = '__all__'

class KategoriLayananSerializer(serializers.ModelSerializer):
    class Meta:
        model = KategoriLayanan
        fields = '__all__'