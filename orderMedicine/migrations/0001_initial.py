# Generated by Django 3.1.7 on 2021-03-24 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_mail', models.CharField(max_length=30)),
                ('ordered_medicine', models.CharField(max_length=10000)),
                ('supplier_name', models.CharField(max_length=100)),
            ],
        ),
    ]
