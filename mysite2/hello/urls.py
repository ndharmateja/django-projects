from django.urls import path

from . import views

app_name = "hello"

urlpatterns = [
    # /hello/
    path("", views.myview, name="myview"),
]
