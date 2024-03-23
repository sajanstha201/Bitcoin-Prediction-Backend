from django.db import models
class BitcoinConversion(models.Model):
    currency = models.CharField(max_length=10, blank=True, null=True)
    price_per_bitcoin = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bitcoin_conversion'
        app_label='api'

class Query(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Query'
        app_label='api'
class Faq(models.Model):
    question = models.TextField(blank=True, null=True)
    answer = models.TextField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'Faq'
        app_label='api'
