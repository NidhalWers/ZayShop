# Generated by Django 4.0.4 on 2022-05-20 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_apparel_footwear'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='link',
            field=models.TextField(default=''),
        ),
    ]
