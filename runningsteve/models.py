import datetime

from django.db import models
from django.utils import timezone

# Create your models here.


class Runner(models.Model):
    first_name = models.CharField('First Name', max_length=25, null=True)
    second_name = models.CharField('Second Name', max_length=25)
    last_name = models.CharField('Last Name', max_length=25, null=True)
    gender = models.CharField('Gender', max_length=6, null=True)
    date_of_birth = models.DateField('Date of Birth', null=True)

    def __str__(self):
        return f"{self.first_name, self.last_name, self.gender}"

    def __repr__(self):
        return (f"{self.__class__.__name__}"
                f"({self.first_name}, birthyear: {self.date_of_birth}, gender: {self.gender})")


class Race(models.Model):
    TERRAIN_TYPES = (
        (0, 'Road'),
        (1, 'Trail'),
        (2, 'Multi')
    )
    race_name = models.CharField('Race', max_length=40)
    route_name = models.CharField('Route', max_length=20, null=True)
    route_distance = models.FloatField('Distance', null=True)
    route_units = models.CharField('Units', max_length=5)
    terrain = models.IntegerField('Terrain', null=True, choices=TERRAIN_TYPES, default=0)
    race_date = models.DateTimeField('Date', null=True)
    runner = models.ForeignKey(Runner, on_delete=models.CASCADE, null=True, default=1)

    def __str__(self):
        # return self.race_name, self.race_date, self.route_length, self.terrain, self.race_date, self.runner
        return f"{self.race_name, self.route_name, self.route_distance, self.terrain, self.race_date, self.runner}"

    def __repr__(self):
        # return self.race_name, self.race_date, self.route_length, self.terrain, self.race_date, self.runner
        return f"{self.race_name, self.route_name, self.route_distance, self.terrain, self.race_date, self.runner}"
