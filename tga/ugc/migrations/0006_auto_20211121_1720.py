# Generated by Django 2.2.7 on 2021-11-21 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ugc', '0005_auto_20211121_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='thing_type',
            field=models.CharField(max_length=256, verbose_name='Что хранить'),
        ),
    ]
