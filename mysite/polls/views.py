from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here.
def index(_: HttpRequest):


def detail(_: HttpResponse, question_id: int):
    return HttpResponse(f"You're looking at question {question_id}")


def results(_: HttpResponse, question_id):
    return HttpResponse(f"You're looking at the results of question {question_id}")


def vote(_: HttpResponse, question_id):
    return HttpResponse(f"You're voting on question {question_id}")
