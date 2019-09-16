from django.contrib import admin

from django.contrib import admin

from memcache_server.cache.models import Cache


@admin.register(Cache)
class CacheAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Cache._meta.fields]
    search_fields = ['key']
