from rest_framework.routers import DefaultRouter

from memcache_server.cache.views import CacheViewSet

router = DefaultRouter()
router.register(r'cache', CacheViewSet, base_name='cache_values')

urlpatterns = router.urls
