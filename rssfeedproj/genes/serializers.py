from rest_framework import serializers

from genes.models import Gene, Disease


class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease
        fields = ('name', 'risk')

class GeneSerializer(serializers.ModelSerializer):
    risk_categories = DiseaseSerializer(many = True, read_only=True)
    class Meta:
        model = Gene
        fields = ('name', 'risk_categories')    
