# Generated by Django 3.2 on 2021-04-22 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0006_medicinetransaction_is_first_entry'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicinetransaction',
            name='is_first_entry',
        ),
    ]
