# Generated by Django 4.2.1 on 2023-06-04 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='product_reference',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transaction.product'),
        ),
    ]
