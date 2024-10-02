"""
Views
"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from django.core.cache import cache
from .models import RssCache, RssCacheEsp
from .serializers import RSSItemSerializer


class RSSFeedView(APIView):
    """
    View to return RSS feed data based on language.
    It checks if the data is cached. If not, it fetches the data from the
    appropriate database,
    serializes it, and caches it for 15 minutes.
    """
    renderer_classes = [JSONRenderer]

    def get(self, request, language):
        """
        Endpoint to return RSS feed data based on the specified language.
        It checks if the data is cached. If not, it fetches the data from the 
        appropriate database,
        serializes it, and caches it for 15 minutes.
        """
        if language == 'en':
            cache_key = 'rss_feed_data'
        else:
            cache_key = 'rss_feed_data_esp'
        cached_data = cache.get(cache_key)

        if cached_data is None:
            if language == 'en':
                items = RssCache.objects.all().order_by('-pub_date')
            elif language == 'esp':
                items = RssCacheEsp.objects.all().order_by('-pub_date')
            else:
                return Response({'error': 'Page Not Found'}, status=404)

            serializer = RSSItemSerializer(items, many=True)
            cached_data = serializer.data
            cache.set(cache_key, cached_data, 60 * 15)

        return Response(cached_data)
