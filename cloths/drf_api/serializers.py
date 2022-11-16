from rest_framework import serializers
from store.models import ClothsData


class ClothesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClothsData
        fields = '__all__'

