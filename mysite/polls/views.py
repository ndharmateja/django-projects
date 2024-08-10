from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render
from polls.models import Question


# Create your views here.
def index(request: HttpRequest):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    ctx = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", ctx)


def detail(request: HttpResponse, question_id: int):
    try:
        q = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404(f"Question {question_id} does not exist.")

    ctx = {"question": q}
    return render(request, "polls/detail.html", ctx)


def results(_: HttpResponse, question_id):
    return HttpResponse(f"You're looking at the results of question {question_id}")


def vote(_: HttpResponse, question_id):
    return HttpResponse(f"You're voting on question {question_id}")
