# Generated by Django 2.1.2 on 2018-10-24 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('runningsteve', '0003_auto_20181024_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='race',
            name='race_name',
            field=models.CharField(max_length=40, verbose_name='Race'),
        ),
    ]
