"""
URLs
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from genes.views import GeneViewSet
from rssfeed.views import RSSFeedView

router = DefaultRouter()
router.register("result", GeneViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('rss-feed/<str:language>/', RSSFeedView.as_view(), name='rss_feed'),
]
