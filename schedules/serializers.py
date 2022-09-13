from rest_framework import serializers
from schedules.models import Schedule
from courts.serializers import ReturnCourtNameSerializer

import ipdb

from users.serializers import UserBaseInfoSerializer

class ScheduleSerializer(serializers.ModelSerializer):    
    user = UserBaseInfoSerializer(read_only=True) 
    court = ReturnCourtNameSerializer(read_only=True)
    class Meta:
        model = Schedule
        fields = ["id", "datetime", "user", "court"]
        read_only_fields = ["user", "court"]
        
