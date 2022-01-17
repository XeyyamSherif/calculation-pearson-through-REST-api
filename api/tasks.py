from .serializers import user_dataSerializer


def check_validation(data, type, operation):
    list = []
    for item in data['data'][''+type+'']:
        person = {
            "id": 1,
            "user_id": data['user_id'],
            "types_of_data": data['data'][''+type+'_data_type'],
            "date_of_data": item['date'],
            "value": item['value']
        }
        list.append(person)
    serializer = user_dataSerializer(data=list, many=True)

    if serializer.is_valid():

        if operation == 'save':
            serializer.save()
        else:
            return True
    else:
        return serializer.errors
