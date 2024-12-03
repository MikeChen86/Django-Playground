from rest_framework import serializers, views
from restful_api.models import Journey


class JourneySerializer(serializers.HyperlinkedModelSerializer):
    creator = serializers.StringRelatedField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    updated_at = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

    def create(self, validated_data):
        journey = Journey(**validated_data)
        journey.creator = self.context['request'].user
        journey.save()
        return journey

    class Meta:
        model = Journey
        fields = ['url', 'name', 'start_date', 'end_date', 'creator', 'created_at', 'updated_at']
