# Generated by Django 4.0.3 on 2022-12-06 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produse', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
