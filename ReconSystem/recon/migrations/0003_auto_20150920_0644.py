# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recon', '0002_order_net_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='base_price',
        ),
        migrations.AlterField(
            model_name='order',
            name='logistic_fee',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='market_fee',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_collection_fee',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
            preserve_default=True,
        ),
    ]
