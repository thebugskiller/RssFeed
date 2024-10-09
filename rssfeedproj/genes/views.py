from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

from genes.models import Gene, RiskLevel
from genes.serializers import GeneSerializer

# Create your views here.
class GeneViewSet(viewsets.ModelViewSet):
    queryset = Gene.objects.prefetch_related('risk_categories').all()


    def list(self, request):
        genes = Gene.objects.prefetch_related('risk_categories').all()

        def categorize_gene(gene):
            risks = [disease.risk for disease in gene.risk_categories.all()]
            if 'high' in risks:
                return 'high' if 'inconclusive' not in risks else 'high_inconclusive'
            elif 'inconclusive' in risks:
                return 'inconclusive'
            else:
                return 'low'

        def count_risks(gene, risk_type):
            return gene.risk_categories.filter(risk=risk_type).count()

        categorized_genes = {
            'high': [],
            'high_inconclusive': [],
            'inconclusive': [],
            'low': []
        }

        for gene in genes:
            category = categorize_gene(gene)
            if category == 'high':
                categorized_genes['high'].append((gene, count_risks(gene, 'high')))
            elif category == 'high_inconclusive':
                categorized_genes['high_inconclusive'].append((gene, count_risks(gene, 'high')))
            elif category == 'inconclusive':
                categorized_genes['inconclusive'].append((gene, count_risks(gene, 'inconclusive')))
            else:
                categorized_genes['low'].append((gene, count_risks(gene, 'low')))

        for category in categorized_genes:
            categorized_genes[category].sort(key=lambda x: x[1], reverse=True)
        
        response_data = {
            'high_risk': [GeneSerializer(gene[0]).data for gene in categorized_genes['high']],
            'high_risk_and_inconclusive': [GeneSerializer(gene[0]).data for gene in categorized_genes['high_inconclusive']],
            'inconclusive_no_high_risk': [GeneSerializer(gene[0]).data for gene in categorized_genes['inconclusive']],
            'low_risk_only': [GeneSerializer(gene[0]).data for gene in categorized_genes['low']]
        }

        return Response(response_data)
