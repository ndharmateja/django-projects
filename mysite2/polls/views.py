from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from django.urls import reverse
from django.views.generic import DetailView, ListView

from .models import Choice, Question


class QuestionListView(ListView):
    model = Question

    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]


class QuestionDetailView(DetailView):
    model = Question
    template_name = "polls/detail.html"


class QuestionResultsView(DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request: HttpRequest, question_id) -> HttpResponse:
    question: Question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        ctx = {"question": question, "error_message": "You didn't select a choice."}
        return render(request, "polls/detail.html", ctx)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return redirect(reverse("polls:results", args=(question.id,)))


def owner(request: HttpRequest) -> HttpResponse:
    response = HttpResponse()
    response.write("Hello, world. 623d5ca4 is the polls index.")
    return response
