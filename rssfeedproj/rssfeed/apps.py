from django.apps import AppConfig
from django.db.models.signals import post_migrate

from celery import shared_task
import os

class RssfeedConfig(AppConfig):
    """
    This is the application configuration class for the 'rssfeed' app.
    It defines the app's default auto field and connects the post-migrate
    signal to a custom function for creating periodic tasks.
    """
    
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'rssfeed'

    def ready(self):
        """
        This method is called when the app is ready (i.e., loaded and
        initialized).
        It connects the `post_migrate` signal to the `create_periodic_task`
        function, ensuring that the function is triggered after migrations are
        run for this app.
        """
            
        post_migrate.connect(create_periodic_task, sender=self)


def create_periodic_task(sender, **kwargs):
    """
    Creates a periodic Celery task to update the RSS feed every 15 minutes
    after the migration of the 'rssfeed' app is completed.
    """
    from django_celery_beat.models import PeriodicTask, IntervalSchedule  
    from rssfeed.tasks import update_rss_feed
        
    if sender.name == 'rssfeed':
        schedule, created = IntervalSchedule.objects.get_or_create(
            every=15,
            period=IntervalSchedule.MINUTES,
        )

        PeriodicTask.objects.get_or_create(
            interval=schedule,
            name='Update RSS Feed Every 15 Minutes',
            task='rssfeed.tasks.update_rss_feed',
        )
        print("Periodic task created.")
        update_rss_feed.delay()


@shared_task
def update_rss_feed():
    """
    Celery task to update the RSS feed cache with both English and translated
    Spanish entries.
    """
    from django.core.cache import cache
    import feedparser
    from googletrans import Translator
    from datetime import datetime
    from .models import RssCache, RssCacheEsp

    cache_key_eng = 'rss_feed_data_eng'
    cache_key_esp = 'rss_feed_data_esp'
    cache_timeout = 15 * 60
    translator = Translator()

    print("Called update_rss_feed task")

    if cache.get(cache_key_eng) and cache.get(cache_key_esp):
        return

    FEED_URL = os.environ.get('FEED_URL', 'https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml')
    feed_url = FEED_URL
    feed = feedparser.parse(feed_url)

    for entry in feed.entries:
        creator = entry.get('author', '') or entry.get('dc_creator', '')

        image_url = ''
        if 'media_content' in entry:
            media_content = entry.get('media_content', [])
            if media_content and isinstance(media_content, list):
                image_url = media_content[0].get('url', '')

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

        translated_title = translator.translate(entry.title, dest='es').text
        translated_description = translator.translate(entry.description, dest='es').text

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

    cache.set(cache_key_eng, True, cache_timeout)
    cache.set(cache_key_esp, True, cache_timeout)
