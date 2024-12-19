from django.db import models

class BaseStructure(models.Model):
    code = models.CharField(
        max_length=50,
        primary_key=True
        )
    class Meta:
        abstract = True

class Nasdaq(BaseStructure):
    class Meta:
        verbose_name = "Nasdaq Stock"
class Kospi(BaseStructure):
    class Meta:
        verbose_name = "Kospi Stock"
class Kosdaq(BaseStructure):
    class Meta:
        verbose_name = "Kosdaq Stock"

# 주식 데이터의 기본 구조
class Stock_Structure(models.Model):
    date = models.DateField(auto_now=True)
    per = models.FloatField(null=False, blank=False)
    pbr = models.FloatField(null=False, blank=False)
    eps = models.FloatField(null=False, blank=False)
    roe = models.FloatField(null=False, blank=False)
    disclosure = models.ForeignKey(
        'Disclosure',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    class Meta:
        abstract = True

class Nasdaq_Stock(Stock_Structure):
    stock = models.ForeignKey(
        Nasdaq,
        on_delete=models.CASCADE,
        related_name='stock_data' #역방향 참조 시 사용
    )
    
class Kospi_Stock(Stock_Structure):
    stock = models.ForeignKey(
        Kospi,
        on_delete=models.CASCADE,
        related_name='stock_data'
    )

class Kosdaq_Stock(Stock_Structure):
    stock = models.ForeignKey(
        Kosdaq,
        on_delete=models.CASCADE,
        related_name='stock_data'
    )