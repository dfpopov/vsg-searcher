from rest_framework import serializers

class AnimeSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=64)
    image_url = serializers.CharField(max_length=64)
    url = serializers.CharField(max_length=128)
    rating = serializers.CharField(max_length=64)
    popularity = serializers.IntegerField(min_value=0)
    rank = serializers.IntegerField(min_value=0)

    def to_internal_value(self, data):
        data['image_url'] = data['images']['jpg']['large_image_url']
        return data