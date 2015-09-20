# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('channel', models.CharField(max_length=20, choices=[(b'amazon', b'amazon'), (b'paytm', b'paytm'), (b'snapdeal', b'snapdeal'), (b'flipkart', b'flipkart'), (b'ebay', b'ebay')])),
                ('sale_date', models.DateField()),
                ('order_number', models.CharField(unique=True, max_length=200)),
                ('invoice_number', models.CharField(unique=True, max_length=200)),
                ('item', models.TextField(max_length=1000)),
                ('quantity', models.PositiveIntegerField()),
                ('customer_name', models.CharField(max_length=200)),
                ('customer_city', models.CharField(max_length=200)),
                ('base_price', models.FloatField()),
                ('sale_tax_rate', models.FloatField()),
                ('sale_price', models.FloatField()),
                ('market_fee', models.FloatField()),
                ('logistic_fee', models.FloatField()),
                ('payment_collection_fee', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('channel', models.CharField(max_length=20, choices=[(b'amazon', b'amazon'), (b'paytm', b'paytm'), (b'snapdeal', b'snapdeal'), (b'flipkart', b'flipkart'), (b'ebay', b'ebay')])),
                ('pay_date', models.DateField()),
                ('order_number', models.CharField(unique=True, max_length=200)),
                ('item', models.TextField(max_length=1000)),
                ('quantity', models.PositiveIntegerField()),
                ('payment_amount', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Return',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('channel', models.CharField(max_length=20, choices=[(b'amazon', b'amazon'), (b'paytm', b'paytm'), (b'snapdeal', b'snapdeal'), (b'flipkart', b'flipkart'), (b'ebay', b'ebay')])),
                ('return_date', models.DateField()),
                ('order_number', models.CharField(unique=True, max_length=200)),
                ('item', models.TextField(max_length=1000)),
                ('quantity', models.PositiveIntegerField()),
                ('condition', models.CharField(max_length=20, choices=[(b'good', b'good'), (b'damaged', b'damaged')])),
                ('return_amount', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
