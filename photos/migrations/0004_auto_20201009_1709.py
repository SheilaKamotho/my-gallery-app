# Generated by Django 3.1.2 on 2020-10-09 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_auto_20201009_1225'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='photo',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image_description',
            field=models.TextField(),
        ),
    ]
