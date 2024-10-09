import json
from django.core.management.base import BaseCommand
from genes.models import Gene
from django.db import transaction


class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):
        with open("Add fixture json file path here, like below commented code") as f:
        # with open("/Users/dev/Desktop/RssFeed/rssfeedproj/genes/fixtures.json") as f:
            data = json.load(f)
            try:
                with transaction.atomic():
                    for entry in data:
                        gene = Gene.objects.filter(name=entry.get("gene"))
                        print(gene)
                        if not gene:
                            print(entry.get("gene"))
                            gene = Gene(name=entry.get("gene"))
                            gene.save()
                        for risk_category in entry.get("riskCategories"):
                            print(risk_category.get("condition"))
                            disease = gene.risk_categories.all().filter(name=risk_category.get("condition"))
                            print(disease)
                            if not disease:
                                gene.risk_categories.create(name=risk_category.get("condition"), risk=risk_category.get("risk"))
                                gene.save()
            except Exception as e:
                print(e)
