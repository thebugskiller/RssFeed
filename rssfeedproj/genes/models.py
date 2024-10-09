from django.db import models

# Create your models here.

class RiskLevel(models.TextChoices):
    HIGH = "high"
    LOW = "low"
    INCONCLUSIVE = "inconclusive"

class Disease(models.Model):
    name = models.CharField(max_length=255)
    risk = models.CharField(max_length=255, choices=RiskLevel.choices, default=RiskLevel.INCONCLUSIVE)


class Gene(models.Model):
    name = models.CharField(max_length=255, unique=True)
    risk_categories = models.ManyToManyField(Disease, related_name="genes")
