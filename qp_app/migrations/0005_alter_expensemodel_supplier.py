# Generated by Django 5.2 on 2025-04-24 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qp_app', '0004_paymenttype_remove_expensemodel_barcode_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expensemodel',
            name='supplier',
            field=models.CharField(default='none', max_length=50),
        ),
    ]
