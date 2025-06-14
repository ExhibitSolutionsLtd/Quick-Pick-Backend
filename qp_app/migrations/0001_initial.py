# Generated by Django 5.2 on 2025-04-23 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barcode', models.CharField(max_length=12)),
                ('added_by', models.CharField(default='', max_length=100)),
                ('naming', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('buying_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('selling_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('quantity', models.IntegerField(default=0)),
            ],
        ),
    ]
