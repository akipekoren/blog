# Generated by Django 3.1.7 on 2021-05-08 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0019_auto_20210508_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='djangodbmodelsfieldscharfield'),
        ),
    ]
