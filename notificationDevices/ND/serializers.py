from rest_framework import serializers
from .models import Device

# class DeviceSerializers(serializers.Serializer):
#     name = serializers.CharField(max_length= 100)
#     deviceType = serializers.BooleanField()
#     adress = serializers.CharField(max_length= 100)
#     latitude = serializers.DecimalField(max_digits = 9, decimal_places = 6)
#     longtitude = serializers.DecimalField(max_digits = 9, decimal_places = 6)
#     soundRadius = serializers.IntegerField()

#     def create(self, validated_data):
#         return Device.objects.create(validated_data)
class DeviceModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['name', 'deviceType', 'adress', 'latitude', 'longtitude','soundRadius']