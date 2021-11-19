from django.db import models
from django.contrib.gis.db.models import PointField


class CoordinatesModel(models.Model):
    coordinates = PointField()

