# Generated by Django 2.1.5 on 2019-03-31 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SBlokz', '0002_order_hash_id'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='order',
            unique_together={('hash_id',)},
        ),
    ]
