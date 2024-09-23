from django.db import models


class RealState(models.Model):
    REAL_STATE_TYPE = [
        ("House", "House"),
        ("Apartment", "Apartment"),
        ("Office", "Office"),
        ("Land", "Land"),
    ]

    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    type = models.CharField(max_length=50, choices=REAL_STATE_TYPE)
    area = models.DecimalField(max_digits=10, decimal_places=2)
