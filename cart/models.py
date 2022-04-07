from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from hurtownia.models import Produkty


class KupnoAddress(models.Model):
    produkt = models.ForeignKey(Produkty, null=True, on_delete=models.CASCADE)
    klijent = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    address = models.CharField(max_length=200, null=True)
    miasto = models.CharField(max_length=200, null=True)
    kod_pocztowy = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
