from django.shortcuts import render
#from django.http import JsonResponse
from django.http.response import JsonResponse
from django.http import HttpResponse
from time import time 
import csv
import json

model1 = "WS-0001"
model2 = "WS-0002"
model3 = "WS-0003"
model4 = "WS-0004"
Char = '#'
N = 5


def trim_data(data):
    return data.strip()


def padToMultiple(data):
    for i in range(5):
        data = data + Char
    
    return data

def addTimestamp():
    return int(time())

def index(request):
    if request.method == 'GET':
        json_data = json.loads(request.body)
        if json_data['model'] == model1:
            print(json_data)
            return JsonResponse(json_data)
        elif json_data['model'] == model2:
            payload = padToMultiple(json_data['payload'])
            print(payload)
            json_data['payload'] = payload
            return JsonResponse(json_data)
            #return HttpResponse(payload)
        elif json_data['model'] == model3:
            result = trim_data(json_data['payload'])
            payload = padToMultiple(result)
            json_data['payload'] = payload
            with open('logs.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([json_data['sensor_id'], json_data['model'], json_data['payload']])
            return HttpResponse("")
            #print(payload)
        elif json_data['model'] == model4:
            result = trim_data(json_data['payload'])
            payload = padToMultiple(result)
            payload = payload + '_' + str(addTimestamp())
            print(payload)
            json_data['payload'] = payload
            with open('logs.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([json_data['sensor_id'], json_data['model'], json_data['payload']])
            return JsonResponse(json_data)
        else:
            print("This is not a registered model.")


        #return json_data
        return JsonResponse(json_data)
