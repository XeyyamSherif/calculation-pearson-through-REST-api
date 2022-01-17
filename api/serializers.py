from pyexpat import model
from django.db import models
from rest_framework import fields, serializers
from .models import user_data, result_cor


class user_dataSerializer(serializers.ModelSerializer):
    class Meta:

        model = user_data
        fields = ('id', 'user_id', 'types_of_data', 'value', 'date_of_data')


class resultSerializer(serializers.ModelSerializer):

    class Meta:
        model = result_cor
        fields = ('user_id', 'x_data_type', 'y_data_type', 'value', 'p_value')
