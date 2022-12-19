from django.db import models

# Create your models here.
class Lead(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    phone = models.CharField(max_length=60)
    product_id = models.IntegerField()

class Costumer(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    phone = models.CharField(max_length=60)
    address = models.CharField(max_length=60)
    job = models.CharField(max_length=60)
    cpf = models.CharField(max_length=60)
    cnpj = models.CharField(max_length=60)