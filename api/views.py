from datetime import datetime
from unittest import result
from django.shortcuts import render
from django.http import JsonResponse
from django.http.response import HttpResponse
from rest_framework import serializers
from rest_framework.response import Response
from .serializers import user_dataSerializer, resultSerializer
from rest_framework.decorators import api_view
from .models import user_data, result_cor
import numpy as np
from scipy.stats import pearsonr
from .tasks import check_validation


@api_view(["POST"])
def Post_Data(request):
    data = request.data

    if check_validation(data, "x", "check") == True and check_validation(data, "y", "check") == True:
        check_validation(data, "x", "save")
        check_validation(data, "y", "save")
        return Response({
            'message': 'added'
        })
    else:
        return Response({
            'message': 'wrong data type'
        })


@api_view(["GET", "POST"])
def correllation(request):
    x_type = request.GET['x_type']
    y_type = request.GET['y_type']
    user_id = request.GET['user_id']

    if request.method == 'POST':
        user_x_data = user_data.objects.filter(
            user_id=user_id, types_of_data=x_type)
        user_y_data = user_data.objects.filter(
            user_id=user_id, types_of_data=y_type)

        x_type_list = np.array([
            item.value for item in user_x_data if item.value is not None])
        y_type_list = np.array([
            item.value for item in user_y_data if item.value is not None])

        try:
            pearson = pearsonr(x_type_list, y_type_list)
            print(pearson)
        except:
            return Response({
                'error': 'error on pearson calculation'})

        result = {
            "user_id": user_id,
            "x_data_type": x_type,
            "y_data_type": y_type,
            "value": pearson[0],
            "p_value": pearson[1]
        }

        serializer = resultSerializer(data=result)
        if serializer.is_valid():
            result_cor.objects.filter(
                x_data_type=x_type, y_data_type=y_type, user_id=user_id).delete()
            serializer.save()
        else:
            print('invalid')
        return Response(serializer.data)
    elif request.method == 'GET':
        if result_cor.objects.filter(user_id=user_id, x_data_type=x_type, y_data_type=y_type).exists():
            data = result_cor.objects.filter(
                user_id=user_id, x_data_type=x_type, y_data_type=y_type)[0]
            serializer = resultSerializer(data)
            return Response(serializer.data)
        else:
            return Response('no such data')
