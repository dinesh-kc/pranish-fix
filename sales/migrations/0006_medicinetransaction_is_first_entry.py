# Generated by Django 3.2 on 2021-04-22 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0005_medicinetransaction_is_final_entry'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicinetransaction',
            name='is_first_entry',
            field=models.BooleanField(default=False),
        ),
    ]