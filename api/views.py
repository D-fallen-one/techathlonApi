from django.shortcuts import render
from django.http import JsonResponse

def default(request):
    data = {
        'name': 'default',
        'function': 'api callback test',
        'status': 'OK',
    }
    return JsonResponse(data)

def defaultWithParams(request,to,frm):
    print(to)
    data = {
        'to': to,
        'from': frm,
    }
    return JsonResponse(data)
