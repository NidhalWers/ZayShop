# Generated by Django 4.0.4 on 2022-06-19 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='paiement',
            field=models.TextField(default=''),
        ),
    ]
