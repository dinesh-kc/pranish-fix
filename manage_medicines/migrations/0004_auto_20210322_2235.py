# Generated by Django 3.1.7 on 2021-03-22 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_medicines', '0003_auto_20210321_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
