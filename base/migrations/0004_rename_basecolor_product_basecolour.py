# Generated by Django 4.0.4 on 2022-06-02 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_product_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='baseColor',
            new_name='baseColour',
        ),
    ]
