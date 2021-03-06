# Generated by Django 4.0.4 on 2022-06-19 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_rename_basecolor_product_basecolour'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('user', models.TextField(default='')),
                ('date', models.TextField(default='')),
                ('total', models.IntegerField(default=0)),
                ('status', models.TextField(default='')),
                ('products', models.TextField(default='')),
                ('city', models.TextField(default='')),
                ('adress', models.TextField(default='')),
                ('zip', models.IntegerField(default=0)),
            ],
        ),
    ]
