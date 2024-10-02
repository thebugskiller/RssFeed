"""
Models
"""
from django.db import models
from django.db.models import Manager


class RssCache(models.Model):
    """
    Model representing an RSS feed entry in English.

    Attributes:
        title (str): The title of the RSS feed entry.
        link (URL): The URL link to the original article.
        description (str): The description or summary of the article.
        pub_date (datetime): The publication date of the article.
        creator (str): The author or creator of the article, optional.
        image_url (URL): The URL of an image associated with the article,
        optional.
        updated_at (datetime): The timestamp when the entry was last updated.
    """
    title = models.CharField(max_length=200)
    link = models.URLField()
    description = models.TextField()
    pub_date = models.DateTimeField()
    creator = models.CharField(max_length=100, null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)


class RssCacheEsp(models.Model):
    """
    Model representing an RSS feed entry in Spanish.

    Attributes:
        title (str): The translated title of the RSS feed entry.
        link (URL): The URL link to the original article.
        description (str): The translated description or summary of the
        article.
        pub_date (datetime): The publication date of the article.
        creator (str): The author or creator of the article, optional.
        image_url (URL): The URL of an image associated with the article,
        optional.
        updated_at (datetime): The timestamp when the entry was last updated.
    """
    title = models.CharField(max_length=200)
    link = models.URLField()
    description = models.TextField()
    pub_date = models.DateTimeField()
    creator = models.CharField(max_length=100, null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
