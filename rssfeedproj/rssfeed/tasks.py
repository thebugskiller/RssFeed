"""
    Cron Job Task
"""
from datetime import datetime
from celery import shared_task
from django.core.cache import cache
import feedparser
from googletrans import Translator
from .models import RssCache, RssCacheEsp
import os


@shared_task
def update_rss_feed():
    """
    Celery task to update the RSS feed cache with both English and translated
    Spanish entries.

    The task fetches the RSS feed from the specified URL, parses the entries,
    and stores the data
    in two Django models (`RssCache` for English and
    `RssCacheEsp` for Spanish).
    It also caches
    the feed data for 15 minutes.

    Steps:
    1. Check if cached data already exists for both English and Spanish
    versions.
    2. Fetch the RSS feed and parse its entries.
    3. Update or create new entries in both `RssCache` and `RssCacheEsp`
    models.
    4. Use the Google Translate API to translate English titles and
    descriptions into Spanish.
    5. Cache the RSS data for 15 minutes.

    Caching:
    - `cache_key_eng`: Cache key for the English RSS data.
    - `cache_key_esp`: Cache key for the Spanish-translated RSS data.
    - Cache timeout is set to 15 minutes.

    Models:
    - `RssCache`: Stores RSS feed entries in English.
    - `RssCacheEsp`: Stores RSS feed entries translated into Spanish.

    Returns:
    - None. The function updates the database and caches the data.
    """

    cache_key_eng = 'rss_feed_data_eng'
    cache_key_esp = 'rss_feed_data_esp'
    cache_timeout = 15 * 60  # Cache timeout in seconds (15 minutes)

    print("Called update_rss_feed task")

    # Check if the RSS feed data is already cached
    if cache.get(cache_key_eng) and cache.get(cache_key_esp):
        return

    # Fetch the RSS feed
    FEED_URL = os.environ.get('FEED_URL', 'https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml')
    feed_url = FEED_URL
    feed = feedparser.parse(feed_url)
    translator = Translator()

    rss_data_eng = []
    rss_data_esp = []

    # Process each entry in the feed
    for entry in feed.entries:
        creator = entry.get('author', '') or entry.get('dc_creator', '')

        # Extract image URL if present
        image_url = ''
        if 'media_content' in entry:
            media_content = entry.get('media_content', [])
            if media_content and isinstance(media_content, list):
                image_url = media_content[0].get('url', '')

        # Update or create English entry in RssCache
        RssCache.objects.update_or_create(
            link=entry.link,
            defaults={
                'title': entry.title,
                'description': entry.description,
                'pub_date': datetime(*entry.published_parsed[:6]),
                'creator': creator,
                'image_url': image_url,
            }
        )
        rss_data_eng.append({
            'title': entry.title,
            'description': entry.description,
            'link': entry.link,
            'pub_date': datetime(*entry.published_parsed[:6]),
            'creator': creator,
            'image_url': image_url,
        })

        # Translate the title and description to Spanish
        translated_title = translator.translate(entry.title, dest='es').text
        translated_description = translator.translate(entry.description,
                                                      dest='es').text

        # Update or create Spanish entry in RssCacheEsp
        RssCacheEsp.objects.update_or_create(
            link=entry.link,
            defaults={
                'title': translated_title,
                'description': translated_description,
                'pub_date': datetime(*entry.published_parsed[:6]),
                'creator': creator,
                'image_url': image_url,
            }
        )
        rss_data_esp.append({
            'title': translated_title,
            'description': translated_description,
            'link': entry.link,
            'pub_date': datetime(*entry.published_parsed[:6]),
            'creator': creator,
            'image_url': image_url,
        })

    # Cache the fetched RSS data
    cache.set(cache_key_eng, rss_data_eng, cache_timeout)
    cache.set(cache_key_esp, rss_data_esp, cache_timeout)
