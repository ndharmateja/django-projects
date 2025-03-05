from django.urls import path

from . import views

app_name = "polls"

urlpatterns = [
    # /polls/
    path("", views.QuestionListView.as_view(), name="index"),
    # /polls/5/
    path("<int:pk>/", views.QuestionDetailView.as_view(), name="detail"),
    # /polls/5/results
    path(
        "<int:pk>/results/",
        views.QuestionResultsView.as_view(),
        name="results",
    ),
    # /polls/5/vote
    path("<int:question_id>/vote/", views.vote, name="vote"),
    # /polls/owner
    path("owner/", views.owner, name="owner"),
]
