from datetime import timezone
from django.db import models

# Create your models here.
class StockOpenings(models.Model):
    description = models.CharField(max_length=100, blank=False)
    units_per_strip= models.IntegerField(blank=False)
    packing= models.CharField(max_length=100, blank=False)
    batch= models.CharField(max_length=100, blank=False)
    mrp_per_strip= models.FloatField(blank=False)
    expiry_date= models.DateField(blank=False)
    imported_strips= models.IntegerField(blank=False)
    date_of_stock_openings= models.DateField(default=timezone.now)

