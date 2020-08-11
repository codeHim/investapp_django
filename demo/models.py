from django.db import models
class Funds(models.Model):
    fund_id = models.AutoField(primary_key=True)
    scheme_code = models.CharField(max_length=10)
    scheme_name = models.CharField(max_length=150)
    isin_div_pay_growth = models.CharField(max_length=20,blank=True)
    isin_div_reinvest = models.CharField(max_length=20,blank=True)
    net_asset_value = models.FloatField(null=False)
    repurchase_price = models.FloatField(null=True)
    sale_price = models.FloatField(null=True)
    date = models.DateField()

    class Meta:
        db_table = 'funds'

class Investment(models.Model):
    invest_id = models.AutoField(primary_key=True)
    fundId = models.ForeignKey(Funds,on_delete=models.CASCADE)
    invested_at = models.DateField(auto_now_add=True)
    units_purchased = models.FloatField()
    total_amount = models.FloatField()

    class Meta:
        db_table = 'investment'