# Generated by Django 2.2.7 on 2021-11-18 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ugc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='passport_id',
            field=models.CharField(max_length=12, verbose_name='Паспортные данные заказчика'),
        ),
    ]
