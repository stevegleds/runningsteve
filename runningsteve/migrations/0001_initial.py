# Generated by Django 2.1.2 on 2019-04-26 05:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('race_name', models.CharField(max_length=40, verbose_name='Race')),
                ('route_name', models.CharField(max_length=20, null=True, verbose_name='Route')),
                ('route_distance', models.FloatField(null=True, verbose_name='Distance')),
                ('route_units', models.CharField(max_length=5, verbose_name='Units')),
                ('terrain', models.IntegerField(choices=[(0, 'Road'), (1, 'Trail'), (2, 'Multi')], default=0, null=True, verbose_name='Terrain')),
                ('race_date', models.DateTimeField(null=True, verbose_name='Date')),
            ],
        ),
        migrations.CreateModel(
            name='Runner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25, null=True, verbose_name='First Name')),
                ('second_name', models.CharField(max_length=25, verbose_name='Second Name')),
                ('last_name', models.CharField(max_length=25, null=True, verbose_name='Last Name')),
                ('gender', models.CharField(max_length=6, null=True, verbose_name='Gender')),
                ('date_of_birth', models.DateField(null=True, verbose_name='Date of Birth')),
            ],
        ),
        migrations.AddField(
            model_name='race',
            name='runner',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='runningsteve.Runner'),
        ),
    ]
