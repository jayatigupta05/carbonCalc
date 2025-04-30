from django.db import models

# Create your models here.
class EmissionFactor(models.Model):
    category = models.CharField(max_length=100)
    unit = models.CharField(max_length=50)
    co2_per_unit = models.FloatField()

    def __str__(self):
        return f"{self.category} ({self.unit})"
    
class Activity(models.Model):
    category = models.CharField(max_length=100)
    value = models.FloatField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.category}: {self.value}"
    