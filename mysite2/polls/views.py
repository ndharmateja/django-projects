from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader

from .models import Choice, Question


# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]

    template = loader.get_template("polls/index.html")
    ctx = {"latest_question_list": latest_question_list}
    return HttpResponse(template.render(ctx, request))


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    ctx = {"question": question}
    return render(request, "polls/detail.html", ctx)


def results(request, question_id):
    return HttpResponse(f"You're looking at the results of question {question_id}")


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")
