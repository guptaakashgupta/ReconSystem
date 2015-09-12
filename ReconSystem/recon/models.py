from django.db import models

# Create your models here.
class Order(models.Model):
    CHANNEL_CHOICES= (
        ('amazon', 'amazon'),
        ('paytm', 'paytm'),
        ('snapdeal', 'snapdeal'),
        ('flipkart', 'flipkart'),
        ('ebay', 'ebay'),
    )
    channel=models.CharField(max_length=20,choices=CHANNEL_CHOICES)
    sale_date=models.DateField()
    order_number=models.CharField(max_length=200,unique=True)
    invoice_number=models.CharField(max_length=200,unique=True)
    item=models.TextField(max_length=1000)
    quantity=models.PositiveIntegerField()
    customer_name=models.CharField(max_length=200)
    customer_city=models.CharField(max_length=200)
    base_price=models.FloatField()
    sale_tax_rate=models.FloatField()
    sale_price=models.FloatField()
    market_fee=models.FloatField()
    logistic_fee=models.FloatField()
    payment_collection_fee=models.FloatField()

    def _net_receivable(self):
        net_amount=self.sale_price - ( self.sale_price*((self.market_fee+self.logistic_fee+self.payment_collection_fee)*self.sale_tax_rate))
        return net_amount

    net_amount=property(_net_receivable)

    def __str__(self):
        return self.channel+'    '+self.order_number+'    '+self.item+'    '+str(self.sale_date)



