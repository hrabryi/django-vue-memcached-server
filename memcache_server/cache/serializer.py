from rest_framework import serializers

from memcache_server.cache.models import Cache


class CacheSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cache
        fields = '__all__'
