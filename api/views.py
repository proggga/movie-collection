""" Views file """
#from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from api.models.movie import Movie
import json

def index(request):
    """ default index method """
    response_data = { 'message' : 'Access Denied', 'code' : '0xFFFF' }
    return HttpResponse(json.dumps(response_data), content_type="application/json")
