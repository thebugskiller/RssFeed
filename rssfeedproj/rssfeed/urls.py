"""
URLs
"""
from django.urls import path
from .views import RSSFeedView

urlpatterns = [
    path('rss-feed/<str:language>/', RSSFeedView.as_view(), name='rss_feed'),
]
