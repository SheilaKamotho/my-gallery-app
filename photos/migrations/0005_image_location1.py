# Generated by Django 3.1.2 on 2020-10-10 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0004_auto_20201009_1709'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='location1',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
