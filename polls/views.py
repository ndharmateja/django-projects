from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here.
def index(_: HttpRequest):
    return HttpResponse("Hello, world. 7ca7066d is the polls index.")
