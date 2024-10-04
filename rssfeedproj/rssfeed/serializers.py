"""
Serializers
"""
from rest_framework import serializers
from .models import RssCache


class RSSItemSerializer(serializers.ModelSerializer):
    """
    Serializer for the RssCache model.

    This serializer converts the RssCache model instances into a
    JSON-compatible format
    and validates the data. It includes the following fields from the model:
    Fields:
        - title: The title of the RSS feed entry.
        - link: The URL link to the article.
        - description: The description or summary of the article.
        - pub_date: The publication date of the article.
        - creator: The author or creator of the article.
        - image_url: The URL of an image associated with the article.
    """
    class Meta:
        """
        Meta class for the RSSItemSerializer.

        This class defines the model and fields to be serialized.

        Attributes:
            model (Type[models.Model]): The model associated with the
            serializer.
            fields (List[str]): The fields of the model to be included in the
            serialization.
        """
        model = RssCache
        fields = [
            'title',
            'link',
            'description',
            'pub_date',
            'creator',
            'image_url'
        ]
