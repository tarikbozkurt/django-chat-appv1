from rest_framework import serializers
from .models import Room

class RoomSerializer(serializers.ModelSerializer):
    class meta:
        model =Room
        fields=('id','code','host','quest_can_pause','votes_to_skip','created_at')


    