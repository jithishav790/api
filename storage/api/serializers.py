from rest_framework import serializers
from .models import *


    # def validate(self,data):
    #     if n in data['LocaationName']:
    #         if n.isdigit():



class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('__all__')


class ItemSerializer(serializers.ModelSerializer):
    itemLocation = LocationSerializer()
    class Meta:
        model = Item
        fields = ('__all__')