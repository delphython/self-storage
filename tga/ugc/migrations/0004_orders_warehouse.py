# Generated by Django 2.2.7 on 2021-11-21 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ugc', '0003_remove_orders_warehouse'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='warehouse',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ugc.Warehouses', verbose_name='Склад'),
        ),
    ]
