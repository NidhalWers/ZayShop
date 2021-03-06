# Generated by Django 4.0.4 on 2022-05-19 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('gender', models.TextField(default='')),
                ('masterCategory', models.TextField(default='')),
                ('subCategory', models.TextField(default='')),
                ('articleType', models.TextField(default='')),
                ('baseColor', models.TextField(default='')),
                ('season', models.TextField(default='')),
                ('year', models.IntegerField(default=0)),
                ('usage', models.TextField(default='')),
                ('productDisplayName', models.TextField(default='')),
                ('price', models.IntegerField(default=0)),
            ],
        ),
    ]
