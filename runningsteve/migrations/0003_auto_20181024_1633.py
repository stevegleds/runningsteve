# Generated by Django 2.1.2 on 2018-10-24 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('runningsteve', '0002_auto_20181024_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='race',
            name='terrain',
            field=models.IntegerField(choices=[(0, 'Road'), (1, 'Trail'), (2, 'Multi')], default=0, null=True, verbose_name='Terrain'),
        ),
    ]