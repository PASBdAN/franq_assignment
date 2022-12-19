from django.db import models

# Create your models here.
class Lead(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    phone = models.CharField(max_length=60)
    product_id = models.IntegerField()