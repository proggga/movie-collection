""" Views file """
#from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import json

def index(request):
    """ default index method """
    response_data = { 'message' : 'This is my api' }
    return HttpResponse(json.dumps(response_data), content_type="application/json")
