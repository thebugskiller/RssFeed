"""
Test Cases
"""
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from rssfeed.models import RssCache, RssCacheEsp


class RSSFeedViewTests(APITestCase):
    """
    Test cases for RSS Feed API views
    """
    
    def setUp(self):
        """
        Set up test data for the RSS Feed tests
        """
        self.english_item = RssCache.objects.create(
            title="Test Article 1",
            link="http://example.com/article1",
            pub_date="2024-01-01T12:00:00Z",
            description="This is a test article."
        )
        self.spanish_item = RssCacheEsp.objects.create(
            title="Artículo de Prueba 1",
            link="http://example.com/articulo1",
            pub_date="2024-01-01T12:00:00Z",
            description="Este es un artículo de prueba."
        )
        
    def test_get_rss_feed(self):
        """
        Test retrieving the RSS feed in English
        """
        response = self.client.get(reverse('rss_feed', args=['en']))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)
        self.assertIn('title', response.data[0])
        self.assertIn('link', response.data[0])
        self.assertIn('description', response.data[0])
        self.assertIn('pub_date', response.data[0])
        self.assertEqual(response.data[0]['title'], self.english_item.title)

    def test_get_rss_feed_esp(self):
        """
        Test retrieving the RSS feed in Spanish
        """
        response = self.client.get(reverse('rss_feed', args=['esp']))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)
        self.assertIn('title', response.data[0])
        self.assertIn('link', response.data[0])
        self.assertIn('description', response.data[0])
        self.assertIn('pub_date', response.data[0])
        self.assertEqual(response.data[0]['title'], self.spanish_item.title)
