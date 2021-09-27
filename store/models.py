from django.db import models

# Create your models here.
class ProductModel(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1023, blank=True)
    rate = models.PositiveSmallIntegerField(default=0)
    number_of_rates = models.PositiveIntegerField(default=0)
    is_available = models.BooleanField(default=False)