# Generated by Django 5.2 on 2025-04-29 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qp_app', '0014_rename_name_company_company_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='company',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='paymenttype',
            old_name='type_name',
            new_name='name',
        ),
    ]
