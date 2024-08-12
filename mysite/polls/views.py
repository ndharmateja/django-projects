from typing import Any

from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from polls.models import Choice, Question


# Create your views here.
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self) -> QuerySet[Any]:
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request: HttpRequest, question_id):
    question = get_object_or_404(Question, pk=question_id)

    # Get the selected choice
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # If error, rerender the question voting form
        ctx = {"question": question, "error_message": "You didn't select a choice"}
        return render(request, "polls/detail.html", ctx)
    else:
        # Increment the selected choice
        selected_choice.votes += 1
        selected_choice.save()

        # Return redirect to avoid form being posted twice
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))


def owner(_: HttpRequest):
    return HttpResponse("Hello, world. 7ca7066d is the polls index.")
