from rest_framework import serializers


class AddParamSerializer(serializers.Serializer):
    value1 = serializers.IntegerField()
    value2 = serializers.IntegerField()
