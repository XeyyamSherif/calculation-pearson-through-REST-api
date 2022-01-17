from urllib import request
from django.db import models
from django.contrib.auth.models import User
from cal_correl import settings
from datetime import datetime


class user_data(models.Model):
    user_id = models.IntegerField()
    types_of_data = models.CharField(max_length=255, null=True)
    value = models.FloatField(null=True)
    date_of_data = models.DateField(default=datetime.today)


class result_cor(models.Model):
    user_id = models.IntegerField()
    x_data_type = models.CharField(max_length=255)
    y_data_type = models.CharField(max_length=255)
    value = models.FloatField(default=1)
    p_value = models.FloatField(default=1)
