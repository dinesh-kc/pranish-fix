# Generated by Django 3.1.2 on 2021-01-12 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('med_name', models.CharField(max_length=30)),
                ('price', models.CharField(max_length=30)),
                ('selling_price', models.CharField(max_length=30)),
                ('supplier', models.CharField(max_length=30)),
                ('bought_date', models.CharField(max_length=30)),
                ('expiry_date', models.CharField(max_length=30)),
                ('time_table', models.CharField(max_length=30)),
            ],
        ),
    ]
