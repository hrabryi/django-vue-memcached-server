from rest_framework import viewsets

from memcache_server.cache.models import Cache
from memcache_server.cache.serializer import CacheSerializer


class CacheViewSet(viewsets.ModelViewSet):
    """
    Returns a list of key-values (cache).
    """
    serializer_class = CacheSerializer
    queryset = Cache.objects.all()

