from rest_framework import serializers
from laundryabc_app.models import PaketLaundry

class PaketLaundrySerializer(serializers.ModelSerializer):
    class Meta:
        model = PaketLaundry
        fields = '__all__'

